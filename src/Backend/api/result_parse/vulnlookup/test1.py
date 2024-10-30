import re

def check_format(string):
    pattern = r'\d+\.\d+(\.\d+)?$'
    if re.match(pattern, string):
        return True
    else:
        return False

# 테스트 문자열
test_string1 = "2.4"
test_string2 = "2.4.11"
test_string3 = "2.*"
test_string4 = "1.1.1."

print(check_format(test_string1))  # True
print(check_format(test_string2))  # True
print(check_format(test_string3))  # False
print(check_format(test_string4))  # False
