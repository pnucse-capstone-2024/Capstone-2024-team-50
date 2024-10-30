import csv

# def parse_vulners_result(text):
#     parsed_data = []
#     header = None
#     for line in text.strip().split('\n'):
#         if ';' in line:
#             if not header:
#                 header = line.strip().split(';')
#             else:
#                 entry_dict = {}
#                 fields = line.strip().split(';')

#                 if fields[0].startswith("PRION:CVE"):
#                     fields[0] = fields[0].replace("PRION:", "")
#                     for i, field in enumerate(fields):
#                         entry_dict[header[i]] = field
#                     parsed_data.append(entry_dict)
#                 elif fields[0].startswith("OSV:BIT-APACHE"):
#                     fields[0] = fields[0].replace("OSV:BIT-APACHE", "CVE")
#                     for i, field in enumerate(fields):
#                         entry_dict[header[i]] = field
#                     parsed_data.append(entry_dict)
#                 elif fields[0].startswith("CVE:"):
#                     for i, field in enumerate(fields):
#                         entry_dict[header[i]] = field
#                     parsed_data.append(entry_dict)
                
#     # 결과 출력
#     return parsed_data

def parse_vulners_result(text):
    parsed_data = []
    header = None
    # CSV가 시작되는 부분을 찾음
    start_parsing = False
    for line in text.strip().split('\n'):
        # 'ID;CVSS;Title;Description;URL;Type'가 있는 줄부터 파싱 시작
        if 'ID;CVSS;Title;Description;URL;Type' in line:
            start_parsing = True
            header = line.strip().split(';')  # 헤더 설정
            continue
        
        if start_parsing:
            if ';' in line:
                entry_dict = {}
                fields = line.strip().split(';')

                if fields[0].startswith("PRION:CVE"):
                    fields[0] = fields[0].replace("PRION:", "")
                    for i, field in enumerate(fields):
                        entry_dict[header[i]] = field
                    parsed_data.append(entry_dict)
                elif fields[0].startswith("OSV:BIT-APACHE"):
                    fields[0] = fields[0].replace("OSV:BIT-APACHE", "CVE")
                    for i, field in enumerate(fields):
                        entry_dict[header[i]] = field
                    parsed_data.append(entry_dict)
                elif fields[0].startswith("CVE-") or fields[0].startswith("cve-"):
                    for i, field in enumerate(fields):
                        entry_dict[header[i]] = field
                    parsed_data.append(entry_dict)
                
    return parsed_data

def parse_exploits_result(text):
    parsed_data = []
    header = None
    for line in text.strip().split('\n'):
        if ';' in line:
            if not header:
                header = line.strip().split(';')
            else:
                entry_dict = {}
                fields = line.strip().split(';')
                if fields[5] == "exploitdb":
                    for i, field in enumerate(fields):
                        entry_dict[header[i]] = field
                    parsed_data.append(entry_dict)

    # 결과 출력
    return parsed_data