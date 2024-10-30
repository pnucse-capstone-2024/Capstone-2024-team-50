import re

# nmap 결과를 파싱하는 함수
def parse_nmap_result(nmap_result):
    # IP 주소 추출
    ip_address = re.search(r"Scanning (\d+\.\d+\.\d+\.\d+)", nmap_result)
    if ip_address:
        ip_address = ip_address.group(1)
    else:
        ip_address = "Unknown"

    # 열린 포트 추출
    open_ports = re.findall(r"Discovered open port (\d+)/(tcp|udp) on \d+\.\d+\.\d+\.\d+", nmap_result)
    open_ports = [(port, protocol) for port, protocol in open_ports]

    # 스캔 타이밍 관련 정보 추출
    timing_info = re.findall(r"hostgroups: .*?min (\d+), max (\d+).*?Completed (Connect|Service) Scan at (\d+:\d+).*?elapsed \((\d+).*? total (ports|services)\)", nmap_result)

    if timing_info:
        min_hostgroups, max_hostgroups, scan_type, scan_time, total_count, unit = timing_info[0]
    else:
        min_hostgroups = max_hostgroups = scan_type = scan_time = total_count = unit = "N/A"

    result_dict = {
        "ip_address": ip_address,
        "open_ports": open_ports,
        "min_hostgroups": min_hostgroups,
        "max_hostgroups": max_hostgroups,
        "scan_type": scan_type,
        "scan_time": scan_time,
        "total_count": total_count,
        "unit": unit
    }

    return result_dict


            # 출력할때 사용
            # print(f"IP Address: {result_parse['ip_address']}")
            # print("Open Ports:")
            # for port, protocol in result_parse['open_ports']:
            #     print(f"   Port: {port}, Protocol: {protocol}")

            # print(f"\nScan Timing Information:")
            # print(f"   Minimum Hostgroups: {result_parse['min_hostgroups']}")
            # print(f"   Maximum Hostgroups: {result_parse['max_hostgroups']}")
            # print(f"   Scan Type: {result_parse['scan_type']} Scan")
            # print(f"   Scan Time: {result_parse['scan_time']}")
            # print(f"   Total {result_parse['scan_type']}: {result_parse['total_count']} {result_parse['unit']}")