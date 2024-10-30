import re
import json

# 예시
# """
#                    ______
#                   /      \\
#                  (  Woof! )
#                   \\  ____/                      )
#                   ,,                           ) (_
#              .-. -    _______                 ( |__|
#             ()``; |==|_______)                .)|__|
#             / ('        /|\\                  (  |__|
#         (  /  )        / | \\                  . |__|
#          \\(_)_))      /  |  \\                   |__|

#                     ~ WAFW00F : v2.2.0 ~
#     The Web Application Firewall Fingerprinting Toolkit

# [*] Checking https://example.org
# [+] The site https://example.org is behind Edgecast (Verizon Digital Media) WAF.
# [~] Number of requests: 5
# """

def parse_wafw00f_result(wafw00f_result):
    # URL과 WAF 이름을 추출하기 위한 정규 표현식 패턴
    pattern = r"Checking\s(https?://[^\s]+).*behind\s(.+?)\sWAF"

    # 정규 표현식을 사용하여 URL과 WAF 이름 추출
    matches = re.findall(pattern, wafw00f_result)

    # URL과 WAF 이름 출력
    for match in matches:
        url = match[0]
        waf = match[1]
        print(f"URL: {url}, WAF: {waf}")

    result = {
        "url": url,
        "waf": waf
    }

    return result