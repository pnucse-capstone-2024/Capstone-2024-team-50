import re

output = """
RHOSTS => 10.10.53.101
RHOST => 10.10.53.101
RPORT => 80
VERBOSE => true
[*] 10.10.53.101 (Apache/2.4.18 (Ubuntu)) WebDAV disabled.
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution complete
"""

# 정규 표현식을 사용하여 호스트의 버전 정보 추출
match = re.search(r'\((.*?)\)', output)
if match:
    version_info = match.group(1)
    print("Host Version Information:", version_info)
else:
    print("Host version information not found.")
