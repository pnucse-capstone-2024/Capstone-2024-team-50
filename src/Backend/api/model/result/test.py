# 기존 딕셔너리
db_host_info = {
    'A': 'B',
    'C': 'D'
}

# 추가할 딕셔너리
host_info = {
    'E': 'F',
    'A': 'X'  # 키 'A'의 값이 변경됨
}

# 업데이트
db_host_info.update(host_info)

print(db_host_info)
