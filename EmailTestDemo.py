import os
import smtplib

EMAIL = "testingstick357@gmail.com"
EMAIL_PASS = "ChapStick357357"

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL, EMAIL_PASS)

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this Saturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL, 'testingstick357@gmail.com', msg)