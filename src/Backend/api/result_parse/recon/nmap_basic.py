import re

def detect_unrecongnized_service(banner):
    pattern = r'^1 service unrecognized despite returning data\..*'
    match = re.search(pattern, banner, re.MULTILINE)
    if match:
        return True
    else:
        return False

def parse_nmap_scan_report(scan_report):
    service_info = {}
    os_info = {}

    # 서비스와 버전 정보 추출 (VERSION 부분이 없을 수도 있음)
    matches = re.findall(r'(\d+)\/(\w+)\s+(\w+)\s+([^\s]+)\s+(.*)', scan_report)
    for match in matches:
        port_num, protocol, state, service, version_info = match
        if detect_unrecongnized_service(version_info):
            version_info = "Unrecognized service"
        port = f"{port_num}/{protocol}"
        service_info[port] = {'state': state, 'service': service, 'version_info': version_info.strip() if version_info else "Unknown"}

    # OS 정보 추출 없으면 ""으로
    os_match = re.search(r'Service Info: OS:\s*(.*?)(;|$)', scan_report, re.MULTILINE)
    if os_match:
        os_info['name'] = os_match.group(1).strip()
    else:
        os_info['name'] = ""

    return service_info, os_info

def parse_nmap_basic(text):
    # Nmap 스캔 보고서 파싱
    service_info, os_info = parse_nmap_scan_report(text)

    port_num = "unknown"
    protocol = "unknown"
    info = {}

    for port, info in service_info.items():
        port_num, protocol = port.split('/')

    tmp = {
        "port": port_num,
        "protocol": protocol,
        "service": info.get('service', 'unknown'),
        "banner": info.get('version_info', 'Unknown').split('\n')[0],
        "os": os_info.get('name', 'Unknown')
    }

    return tmp

# 주어진 Nmap 스캔 보고서
nmap_scan_report = """
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-11 11:00 UTC
Nmap scan report for 192.168.29.131
Host is up (0.00068s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
"""

nmap_scan_report2 = """
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-16 10:29 UTC
Nmap scan report for 192.168.29.129
Host is up (0.00089s latency).

PORT    STATE SERVICE     VERSION
139/tcp open  netbios-ssn Microsoft Windows netbios-ssn
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.55 seconds
"""