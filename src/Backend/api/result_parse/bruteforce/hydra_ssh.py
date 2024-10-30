import re

def parse_hydra_output(output):
    success_match = re.search(r'\[(\d+)\]\[ssh\]\s+host:\s+(\S+)\s+login:\s+(\S+)\s+password:\s+(\S+)', output)
    if success_match:
        port = success_match.group(1)
        host = success_match.group(2)
        username = success_match.group(3)
        password = success_match.group(4)
        return port, host, username, password
    else:
        return None, None, None, None

# 주어진 Hydra 결과
hydra_output = """
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-03-21 15:53:10
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 17 login tries (l:1/p:17), ~2 tries per task
[DATA] attacking ssh://192.168.29.131:22/
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[INFO] Testing if password authentication is supported by ssh://root@192.168.29.131:22
[INFO] Successful, password authentication is supported by ssh://192.168.29.131:22
[ATTEMPT] target 192.168.29.131 - login "root" - pass "root" - 1 of 17 [child 0] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "" - 2 of 17 [child 1] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "toor" - 3 of 17 [child 2] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "java5967301" - 4 of 17 [child 3] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "1234" - 5 of 17 [child 4] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "1" - 6 of 17 [child 5] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "2" - 7 of 17 [child 6] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "3" - 8 of 17 [child 7] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "4" - 9 of 17 [child 8] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "5" - 10 of 17 [child 9] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "6" - 11 of 17 [child 10] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "7" - 12 of 17 [child 11] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "8" - 13 of 17 [child 12] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "9" - 14 of 17 [child 13] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "10" - 15 of 17 [child 14] (0/0)
[ATTEMPT] target 192.168.29.131 - login "root" - pass "12345" - 16 of 17 [child 15] (0/0)
[ERROR] could not connect to target port 22: Socket error: disconnected
[ERROR] ssh protocol error
[ERROR] could not connect to target port 22: Socket error: disconnected
[ERROR] ssh protocol error
[ERROR] could not connect to target port 22: Socket error: disconnected
[ERROR] ssh protocol error
[VERBOSE] Disabled child 0 because of too many errors
[VERBOSE] Disabled child 8 because of too many errors
[VERBOSE] Disabled child 11 because of too many errors
[ATTEMPT] target 192.168.29.131 - login "root" - pass "1q2w3e4r5t" - 17 of 20 [child 1] (0/3)
[22][ssh] host: 192.168.29.131   login: root   password: java5967301
[STATUS] attack finished for 192.168.29.131 (waiting for children to complete tests)
c1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 2 final worker threads did not complete until end.
[ERROR] 2 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-03-21 15:53:14
"""


def parse_hydra_ssh(text):
    # Hydra 결과 파싱
    port, host, username, password = parse_hydra_output(text)

    if port == None:
        return None

    tmp = {
        "port" : port,
        "host" : host,
        "username" : username,
        "password" : password
    }

    return tmp
