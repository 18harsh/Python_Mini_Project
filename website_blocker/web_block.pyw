# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:18:30 2020

@author: Harsh
"""
#program architecture
#mac and linus: /etc/hosts
#windows: C:\Users\Harsh\Desktop\code\10 python project\website_blocker\

import time
from datetime import datetime as dt


hosts_temp = "C:\\Users\\Harsh\\Desktop\\code\\10 python project\\website_blocker\\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.linkedin.com","web.whatsapp.com","www.linkedin.com/feed/","www.google.com/maps","codeshare.io"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,12,00) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23,15):
        print("working hours....")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
            # print(content)
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()        
        print("Fun Hours...")
    time.sleep(5)
    
    