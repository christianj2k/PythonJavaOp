# Random Password Generator

import random
import sys

def passV1(x):
    password = ""
    value = int(x)
    for i in range(value // 2):
        a = chr(random.randint(65,90))
        b = chr(random.randint(65,90))
        c = chr(random.randint(60,71))
        d = chr(random.randint(41,57))
        e = chr(random.randint(65,90)).lower()
        up_low = a + e
        shuffle  =  b + c + d + e
        password = str(password)+ ''.join(random.sample(up_low,len(up_low))) + ''.join(random.sample(shuffle,len(shuffle)))
    if(len(password)>value):
        extra = len(password) - value
        password = password[0:len(password)-extra]
    print("Password: " + password)

if(len(sys.argv) == 1):
    user = input("Enter the character count for the password:\n")
    passV1(user)
else:
    user = sys.argv[1]
    passV1(user)
