import json
import re
# halberd result 문자열 예시

# result_string = """
# INFO looking up host 10.10.251.52...
# INFO host lookup done.

# 10.10.251.52     [          ]  clues:   0 | replies:   0 | missed:   0
# 10.10.251.52     [          ]  clues:   0 | replies:   0 | missed:   0
# 10.10.251.52     [          ]  clues:   0 | replies:   0 | missed:   0
# ...
# 10.10.251.52     [##########]  clues:   2 | replies:  44 | missed:   0

# ======================================================================
# http://10.10.251.52:80 (10.10.251.52): 1 real server(s)
# ======================================================================

# server 1: Apache/2.4.18 (Ubuntu)
# ----------------------------------------------------------------------

# difference: 1 seconds
# successful requests: 44 hits (100.00%)
# header fingerprint: 7997d9f70ce8aa2cad011a0da598a36be04276b2
# """

def parse_halberd_result(halberd_result):
    # 서버 정보를 저장할 리스트 초기화
    servers = []

    # IP 주소, 서비스 상태, 특성 및 서버 정보를 추출하여 리스트에 저장
    server_info_pattern = re.compile(r'server (\d+): ([\w\/.]+)')
    print(1)
    for line in halberd_result.split('\n'):
        if 'server' in line:
            match = server_info_pattern.match(line)
            if match:
                server_number = match.group(1)
                server_description = match.group(2)
                # 서버 설명 파싱하여 서버 이름과 버전 추출
                server_name, server_version = server_description.split('/')
                servers.append({'server_number': server_number, 'server_name': server_name, 'server_version': server_version})
    print(servers)

    return servers

# result_json 형식
# {
#     "servers": [
#         {
#             "server_number": "1",
#             "server_name": "Apache",
#             "server_version": "2.4.18"
#         }
#     ]
# }