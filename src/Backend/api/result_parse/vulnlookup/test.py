# 내가 직접 만든거임

import requests
import re
import argparse
from bs4 import BeautifulSoup
from packaging import version


def extract_first_word(text):
    return text.split(' ')[0]

def check_format(string):
    pattern = r'\d+\.\d+(\.\d+)?$'
    if re.match(pattern, string):
        return True
    else:
        return False


parser = argparse.ArgumentParser(description='CVE Search from https://cve.mitre.org/')
parser.add_argument('--cve', type=str, help='CVE NAME')

args=parser.parse_args()

# 가져올 웹 페이지 URL
url = 'https://cve.mitre.org/cgi-bin/cvename.cgi?name=[CVE_NAME]'

replece_url = re.sub(r'\[CVE_NAME\]', args.cve.lower(), url)

cve_info = []

# URL에 GET 요청을 보냄
response = requests.get(replece_url)

# 응답에서 HTML을 추출
html_content = response.text

# BeautifulSoup을 사용하여 HTML을 파싱
soup = BeautifulSoup(html_content, 'html.parser')

# 필요한 정보 추출
# CVE 번호와 Description 정보 가져오기
tables = soup.find_all('table', {'cellpadding': '0'})

for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 2:
            cve_link = columns[0].find('a')
            if cve_link:
                cve_number = cve_link.text.strip()
                description = columns[1].text.strip()
                tmp_before = f'before'
                before_index = description.find(tmp_before)
                cve_info.append({'CVE Number': cve_number, 'Description': description})

# 결과 출력
for item in cve_info:
    print(item)