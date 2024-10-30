import re


def parse_ssh_info(ssh_info_string):
    parsed_info = {}

    # General information
    general_info = re.findall(r'\(gen\) (\w+):\s(.+)', ssh_info_string)
    parsed_info['general'] = {key: value for key, value in general_info}

    # Key exchange algorithms
    kex_algorithms = re.findall(r'\(kex\) (\S+)\s+(?:-- \[(\w+)\] (.*))?', ssh_info_string)
    parsed_info['key_exchange_algorithms'] = {kex[0]: {'status': kex[1], 'description': kex[2]} if kex[1] else {'status': None, 'description': None} for kex in kex_algorithms}

    # Host-key algorithms
    host_key_algorithms = re.findall(r'\(key\) (\S+)\s+(?:-- \[(\w+)\] (.*))?', ssh_info_string)
    parsed_info['host_key_algorithms'] = {key[0]: {'status': key[1], 'description': key[2]} if key[1] else {'status': None, 'description': None} for key in host_key_algorithms}

    # Encryption algorithms
    encryption_algorithms = re.findall(r'\(enc\) (\S+)\s+(?:-- \[(\w+)\] (.*))?', ssh_info_string)
    parsed_info['encryption_algorithms'] = {enc[0]: {'status': enc[1], 'description': enc[2]} if enc[1] else {'status': None, 'description': None} for enc in encryption_algorithms}

    # Message authentication code algorithms
    mac_algorithms = re.findall(r'\(mac\) (\S+)\s+(?:-- \[(\w+)\] (.*))?', ssh_info_string)
    parsed_info['mac_algorithms'] = {mac[0]: {'status': mac[1], 'description': mac[2]} if mac[1] else {'status': None, 'description': None} for mac in mac_algorithms}

    # Algorithm recommendations
    algorithm_recommendations = re.findall(r'\(rec\) ([\+-]\S+)\s+(.*)', ssh_info_string)
    parsed_info['algorithm_recommendations'] = {rec[0]: rec[1] for rec in algorithm_recommendations}

    return parsed_info

def parse_software_info(software_info):
    # 정규 표현식을 사용하여 이름과 버전을 추출
    match = re.match(r'([\w\s]+)\s+(\d+\.\d+)(?:\w*\d*)?', software_info)
    if match:
        name = match.group(1).strip()
        version = match.group(2)
        return name, version
    else:
        return None, None

ssh_info_string = """
# general
(gen) banner: SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.6
(gen) software: OpenSSH 8.9p1
(gen) compatibility: OpenSSH 7.3+, Dropbear SSH 2016.73+
(gen) compression: enabled (zlib@openssh.com)

# key exchange algorithms
(kex) curve25519-sha256                     -- [warn] unknown algorithm
(kex) curve25519-sha256@libssh.org          -- [info] available since OpenSSH 6.5, Dropbear SSH 2013.62
(kex) ecdh-sha2-nistp256                    -- [fail] using weak elliptic curves
(kex) ecdh-sha2-nistp256                    -- [info] available since OpenSSH 5.7, Dropbear SSH 2013.62
(kex) ecdh-sha2-nistp384                    -- [fail] using weak elliptic curves
(kex) ecdh-sha2-nistp384                    -- [info] available since OpenSSH 5.7, Dropbear SSH 2013.62
(kex) ecdh-sha2-nistp521                    -- [fail] using weak elliptic curves
(kex) ecdh-sha2-nistp521                    -- [info] available since OpenSSH 5.7, Dropbear SSH 2013.62
(kex) sntrup761x25519-sha512@openssh.com    -- [warn] unknown algorithm
(kex) diffie-hellman-group-exchange-sha256  -- [warn] using custom size modulus (possibly weak)
(kex) diffie-hellman-group-exchange-sha256  -- [info] available since OpenSSH 4.4
(kex) diffie-hellman-group16-sha512         -- [info] available since OpenSSH 7.3, Dropbear SSH 2016.73
(kex) diffie-hellman-group18-sha512         -- [info] available since OpenSSH 7.3
(kex) diffie-hellman-group14-sha256         -- [info] available since OpenSSH 7.3, Dropbear SSH 2016.73
(kex) kex-strict-s-v00@openssh.com          -- [warn] unknown algorithm

# host-key algorithms
(key) rsa-sha2-512                          -- [info] available since OpenSSH 7.2
(key) rsa-sha2-256                          -- [info] available since OpenSSH 7.2
(key) ecdsa-sha2-nistp256                   -- [fail] using weak elliptic curves
(key) ecdsa-sha2-nistp256                   -- [warn] using weak random number generator could reveal the key
(key) ecdsa-sha2-nistp256                   -- [info] available since OpenSSH 5.7, Dropbear SSH 2013.62
(key) ssh-ed25519                           -- [info] available since OpenSSH 6.5

# encryption algorithms (ciphers)
(enc) chacha20-poly1305@openssh.com         -- [info] available since OpenSSH 6.5
(enc) chacha20-poly1305@openssh.com         -- [info] default cipher since OpenSSH 6.9.
(enc) aes128-ctr                            -- [info] available since OpenSSH 3.7, Dropbear SSH 0.52
(enc) aes192-ctr                            -- [info] available since OpenSSH 3.7
(enc) aes256-ctr                            -- [info] available since OpenSSH 3.7, Dropbear SSH 0.52
(enc) aes128-gcm@openssh.com                -- [info] available since OpenSSH 6.2
(enc) aes256-gcm@openssh.com                -- [info] available since OpenSSH 6.2

# message authentication code algorithms
(mac) umac-64-etm@openssh.com               -- [warn] using small 64-bit tag size
(mac) umac-64-etm@openssh.com               -- [info] available since OpenSSH 6.2
(mac) umac-128-etm@openssh.com              -- [info] available since OpenSSH 6.2
(mac) hmac-sha2-256-etm@openssh.com         -- [info] available since OpenSSH 6.2
(mac) hmac-sha2-512-etm@openssh.com         -- [info] available since OpenSSH 6.2
(mac) hmac-sha1-etm@openssh.com             -- [warn] using weak hashing algorithm
(mac) hmac-sha1-etm@openssh.com             -- [info] available since OpenSSH 6.2
(mac) umac-64@openssh.com                   -- [warn] using encrypt-and-MAC mode
(mac) umac-64@openssh.com                   -- [warn] using small 64-bit tag size
(mac) umac-64@openssh.com                   -- [info] available since OpenSSH 4.7
(mac) umac-128@openssh.com                  -- [warn] using encrypt-and-MAC mode
(mac) umac-128@openssh.com                  -- [info] available since OpenSSH 6.2
(mac) hmac-sha2-256                         -- [warn] using encrypt-and-MAC mode
(mac) hmac-sha2-256                         -- [info] available since OpenSSH 5.9, Dropbear SSH 2013.56
(mac) hmac-sha2-512                         -- [warn] using encrypt-and-MAC mode
(mac) hmac-sha2-512                         -- [info] available since OpenSSH 5.9, Dropbear SSH 2013.56
(mac) hmac-sha1                             -- [warn] using encrypt-and-MAC mode
(mac) hmac-sha1                             -- [warn] using weak hashing algorithm
(mac) hmac-sha1                             -- [info] available since OpenSSH 2.1.0, Dropbear SSH 0.28

# algorithm recommendations (for OpenSSH 8.9)
(rec) -ecdh-sha2-nistp521                   -- kex algorithm to remove 
(rec) -ecdh-sha2-nistp384                   -- kex algorithm to remove 
(rec) -ecdh-sha2-nistp256                   -- kex algorithm to remove 
(rec) -diffie-hellman-group-exchange-sha256 -- kex algorithm to remove 
(rec) -ecdsa-sha2-nistp256                  -- key algorithm to remove 
(rec) +ssh-rsa                              -- key algorithm to append 
(rec) -hmac-sha2-512                        -- mac algorithm to remove 
(rec) -umac-128@openssh.com                 -- mac algorithm to remove 
(rec) -hmac-sha2-256                        -- mac algorithm to remove 
(rec) -umac-64@openssh.com                  -- mac algorithm to remove 
(rec) -hmac-sha1                            -- mac algorithm to remove 
(rec) -hmac-sha1-etm@openssh.com            -- mac algorithm to remove 
(rec) -umac-64-etm@openssh.com              -- mac algorithm to remove 
"""

def write_sshaudit_result(ssh_info):
    parsed_info = parse_ssh_info(ssh_info)
    software_info = parsed_info.get('general').get('software')
    banner_info = parsed_info.get('general').get('banner')
    software_name, software_version = parse_software_info(software_info)
    if software_name == None:
        return None
    tmp = { 'product' : 
            {
                'name' : software_name,
                'version' : software_version,
                'vendor' : "",
            },
        }

    print(tmp)

    return tmp
