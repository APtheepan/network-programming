import os
import sys
import subprocess
import re


command_output = subprocess.run(["netsh","wlan","show","profile"],capture_output=True).stdout.decode()

profile_name = re.findall('All User Profile     :(.*)\r',command_output)

wifi_list =list()

for name in profile_name:
    profile_info = subprocess.run(["netsh","wlan","show","profile",name],capture_output=True).stdout.decode()
    wifi_profile = dict()
    if re.search('Security key           :Present',profile_info):
        wifi_profile['ssid']=name
        profile_info_pass = subprocess.run(["netsh","wlan","show","profile",name,"key=clear"],capture_output=True).stdout.decode()

        password_info = re.search('Key Content            :(.*)\r',profile_info_pass)
        if password_info == None:
            wifi_profile['password']=None
        else:
            wifi_profile['password']==password_info[1]
            wifi_list.append(wifi_profile)

for x in range(len(wifi_list)):
    print(wifi_list[x])











