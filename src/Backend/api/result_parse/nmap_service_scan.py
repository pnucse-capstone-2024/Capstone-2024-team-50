import re

# Nmap 결과 문자열
nmap_output = """
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-26 12:56 UTC
Nmap scan report for 192.168.29.131
Host is up (0.00091s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
443/tcp  open  https
3306/tcp open  mysql

Nmap done: 1 IP address (1 host up) scanned in 5.57 seconds
"""

def parse_nmap_scan_report(scan_report):
    # 정규 표현식 패턴
    pattern =  r"(\d+)\/(tcp|udp)\s+(\w+)\s+(\w+)"


    # 결과를 저장할 리스트
    parsed_results = []

    # 정규 표현식을 이용한 파싱
    matches = re.findall(pattern, scan_report)

    # 각 매치에서 필요한 정보를 추출하여 리스트에 추가
    for match in matches:
        port = match[0]
        protocol = match[1]
        service = match[3]
        parsed_results.append({"port": port, "protocol": protocol, "service": service})

    # 파싱된 결과 출력
    for result in parsed_results:
        print(result)

    return parsed_results