# cmd : .\Akagi64.exe 45 C:\Windows\System32\cmd.exe
# output : Error executing command: 'Akagi64.exe' 프로그램을 실행하지 못했습니다. 파일에 바이러스 또는 기타 사용자 동의 없이 설치된 소프트웨어가 있기 때문에 작업이 완료되지 않았습니다위치 줄:1 문자:1\n+ .\Akagi64.exe 45 C:\Windows\System32\cmd.exe\n+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.

def windows_command(output: str):
    if 'Error executing command' in output:
        return False
    if '실행되고 있지 않습니다.' in output:
        return False
    if '없습니다.' in output:
        return False

    return True