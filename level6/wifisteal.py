import subprocess
import re

netsh_output = subprocess.check_output("netsh wlan show profile",shell=True).decode('windows-1252')
profile_names = (re.findall("All User Profile     : (.*)\r", netsh_output))
wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:

        wifi_profile = {}

        profile_info = subprocess.check_output("netsh wlan show profile "+name).decode('windows-1252')
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            try:
                wifi_profile["ssid"] = name
                profile_info_pass = subprocess.check_output("netsh wlan show profile "+name+" key=clear").decode('windows-1252')
                password = re.search(
                    "Key Content            : (.*)\r", profile_info_pass)
                if password == None:
                    wifi_profile["password"] = None
                else:
                    wifi_profile["password"] = password[1]
    
                wifi_list.append(wifi_profile)
            except:
                continue

with open("luvpasswords.txt","w") as file:
    for x in range(len(wifi_list)):
        file.write(str(wifi_list[x])+"\n")
    file.close()


