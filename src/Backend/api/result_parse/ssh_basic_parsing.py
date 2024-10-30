import re


# 개선된 정규 표현식 패턴 (특수문자 제외)
pattern = r"(OpenSSH)\s*[^\d]*([0-9]+\.[0-9]+[^\s]*)"

# 소프트웨어 이름과 버전 추출 함수
def extract_software_and_version(string):
    result = {}
    match = re.search(pattern, string)
    if match:
        software, version = match.groups()
        result = {
            "name": software,
            "version": version
        }
    return result
