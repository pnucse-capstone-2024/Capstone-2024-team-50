param(
    [switch]$scan,
    [switch]$on,
    [switch]$off,
    [switch]$pref
)

if ($scan){
   Write-Host "Getting all WIFI networks"
   netsh wlan sh net mode=bssid
} elseif ($on) {
   Write-Host "Turning WIFI on"
   netsh interface set interface name="Wi-Fi" admin=ENABLED
} elseif ($off) {
   Write-Host "Turning WIFI off"
   reg.exe add hkcu\software\classes\ms-settings\shell\open\command /ve /d "C:\Windows\System32\cmd.exe /k powershell netsh interface set interface name='wi-fi' admin=disabled" /f ; reg.exe add hkcu\software\classes\ms-settings\shell\open\command /v "DelegateExecute" /f ; fodhelper.exe
   netsh interface set interface name="Wi-Fi" admin=DISABLED
} elseif ($pref) {
   Write-Host "Getting preferred WIFI networks"
   netsh wlan show profiles
}