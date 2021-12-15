### WINDOWS
### Command: python3 Net_Pass.py

import ssl
import subprocess as sp
import smtplib
import re
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass


#def email_login(s):
   # user_address = input("Input Email Address: ")
    #response = requests.get("https://isitarealemail.com/api/email/validate", params = {'email': user_address})
    #status = response.json()['status']
   # if(status == "valid"):
     #   passwd(user_address, s)
    #    return user_address
   # else:
    #    print("Invalid Email Address, try again")
    #    email_login(s)

def passwd(user_address, s):
        try:
            password = getpass.getpass("Pass: ")
            return password
        except Exception as e:
            print(e)
            #print("An error occured, try again")
            passwd(user_address, s)

def send_email(user_address, SSID_Key, SSID_Cat, s):
    msg = MIMEMultipart()
    name = user_address.split('@')[0]
    email = input("Email address to send key: ")

    msg['From'] = user_address
    msg['TO'] = email
    msg['Subject'] = "The Wifi SSID Key"

    text = 'Wifi Key for SSID: %s\n\n%s' % (SSID_Cat, SSID_Key)
    T1 = MIMEText(text, "plain")
    msg.attach(T1)

    s.send_message(msg)

    del msg

def email_key(SSID_Key, SSID_Cat):
    we_good = False
    while(we_good != True):
        try:
            email_server = input("Type your chosen email server(Ex:gmail.com): ")
            server = 'smtp.%s' % email_server
            store = server + ': 587'
            print(store)
            context = ssl.create_default_context()
            s = smtplib.SMTP(server, 587, None, 30)
            s.ehlo()
            s.starttls(context=context)
            s.ehlo()
            user_email = input("Input Email Address: ")
            Password = getpass.getpass("Pass: ")
            s.login(user_email, Password)
            send_email(user_email, SSID_Key, SSID_Cat, s)
            we_good = True
            Exit = False
            while(Exit == False):
                resend = input("Would you like to email the key again(Y/N): ")
                if(resend == "Y"):
                    send_email(user_email, SSID_Key, SSID_Cat, s)
                elif(resend == "N"):
                    print("Logging out and signing off")
                    s.quit()
                else:
                    print("\nPlease enter Y or N\nTry again")
        except Exception as a:
            print(a)
            Exit = False
            while(Exit == False):
                    retry = input("\nError occured, try again(Y/N): ")
                    if(retry == "Y"):
                        Exit = True
                    elif(retry == "N"):
                        s.quit()
                        sys.exit("\"Exiting program...\"")
                    else:
                        print("\nPlease enter Y or N\nTry again")


def show_pass(SSID_Cat,SSID_Search):
    Permission = sp.run(["netsh", "wlan", "show", "profiles", SSID_Cat, "key=clear"], capture_output = True).stdout.decode()
    Permission_Key = (re.findall("Security key           : (.*)\r", Permission))
    print(Permission_Key)
    if(Permission_Key[0] != "absent"):
        SSID_Key = (re.findall("Key Content            : (.*)\r", Permission))
        print("SSID Network(%s) Key:\n %s" % (SSID_Cat, SSID_Key))
        Exit = False 
        while(Exit == False):
            Decision = input("\nWould you like to email this key(Y/N): ")
            if(Decision == "Y"):
                Exit = True
                email_key(SSID_Key,SSID_Cat)
            elif(Decision == "N"):
                Exit = True
                sys.exit("\"Exiting program...\"")
            else:
                print("\nPlease enter Y or N\nTry again")
    else:  
        print("Permission denied, key is absent\n")
        print("Would you like to enter another SSID?")
        Decision = input("(Y/N): ")
        Exit = False
        while(Exit == False):
            if(Decision == "Y"):
                Exit = True
                Search()
            elif(Decision == "N"):
                Exit = True
                sys.exit("Exiting program")
            else: 
                print("\nPlease enter Y or N\nTry again")
        
def Search():
    SSID_Search = sp.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
    SSID_names = (re.findall("All User Profile     : (.*)\r", SSID_Search))
    if(len(SSID_names) != 0):
            #edit_search = SSID_Search[SSID_Search.find("Profiles"):0]
            print("SSID Networks available on system:\n%s" % SSID_Search)
            Real_Net = False
            while(Real_Net != True):
                SSID_Cat = input("Type chosen Network: ")
                for i in range(len(SSID_names)):
                    if(SSID_names[i] == SSID_Cat):
                        Real_Net = True
                        show_pass(SSID_Cat, SSID_Search)
                if(Real_Net == False):
                    print("\nSSID Network entered does not exist, please try again\n")
        
Search()