import logging
import os
import psutil
from datetime import datetime
import time
from tkinter import *
import random

logging.basicConfig(filename='system_info.log', level=logging.DEBUG)


def info_popup():
    global textBox

    window = Toplevel()
    window.wm_title("Analysing...")
    window.geometry("600x350")

    title = Label(window, text="Analysing...", font=("Roboto", 20))
    title.grid(row=0, column=0)

    textBox = Text(window, width=60, height=20, state='disabled', font=("system", 12))
    textBox.grid(row=1, column=0)


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def getmessage(message):
    global textBox
    textBox.configure(state='normal')
    textBox.insert(1.0, "{message}\n".format(message=message))
    textBox.configure(state='disabled')
    return " {date}; {username}; {message}".format(date=datetime.today().strftime('%Y-%m-%d'),
                                                   username=os.getlogin(), message=message)


def collect_info():
    info_popup()
    global textBox

    textBox.configure(state='normal')
    textBox.delete(1.0, "end-1c")
    textBox.configure(state='disabled')

    try:
        logging.info(getmessage("Logging Session has begun"))

        mem = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        battery = psutil.sensors_battery()
        users = psutil.users()

        logging.debug(getmessage("Total Memory: {mem}".format(mem=mem.total)))
        logging.debug(getmessage("Total Disk: {disk}".format(disk=disk.total)))
        logging.debug(getmessage("Battery Percentage: {battery}".format(battery=battery.percent)))
        logging.debug(getmessage("Battery Remaining: {battery}".format(battery=secs2hours(battery.secsleft))))
        logging.debug(getmessage("Battery Plugged in: {battery}".format(battery=battery.power_plugged)))
        logging.debug(getmessage("List of User Names:"))
        for row in users:
            logging.debug(getmessage(row.name))

        logging.info(getmessage("Logging Session has ended"))
    except Exception as e:
        logging.error(getmessage("Exception Occurred: '{e}'".format(e=e)))
        textBox.configure(state='normal')
        textBox.insert(1.0, "ERROR: EXCEPTION OCCURRED, PLEASE TRY AGAIN LATER\n")
        textBox.configure(state='disabled')
        time.sleep(3)


def update():
    global collect_button
    global chkValue

    new_value = chkValue.get()

    if new_value is True:
        collect_button.configure(state="normal")
    elif new_value is False:
        collect_button.configure(state="disabled")


def get_info():
    info = Toplevel()
    info.wm_title("Information")
    info.geometry("1500x550")

    title = Label(info, text="More Information:", font=("Roboto", 20))
    title.grid(row=0, column=1)

    license_title = Label(info, text="License:", font=("Roboto", 18))
    license_title.grid(row=1, column=0)

    license_info = Label(info, text='Copyright 2019 Daniel Pavela\n'
                                    'Permission is hereby granted, free of charge, to any person\n'
                                    'obtaining a copy of this software and associated documentation files\n'
                                    '(the "Software"), to deal in the Software without restriction, including\n'
                                    'without limitation the rights to use, copy, modify, merge, publish,\n'
                                    'distribute, sublicense, and/or sell copies of the Software, and to\n'
                                    'permit persons to whom the Software is furnished to do so, subject\n'
                                    'to the following conditions:\n\n'
                                    'The above copyright notice and this permission notice shall be included in all\n'
                                    'copies or substantial portions of the Software.\n'
                                    'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,\n'
                                    'INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A\n'
                                    ' PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\n'
                                    'COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,\n'
                                    'WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF\n'
                                    'OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.', font=("Times New Roman", 12))
    license_info.grid(row=2, column=0)

    information_title = Label(info, text="What is being collected:", font=("Roboto", 18))
    information_title.grid(row=1, column=2)

    information_info = Label(info, text="• Total CPU\n"
                                        "• Total RAM\n"
                                        "• Total Storage / Disk\n"
                                        "• Battery Percentage\n"
                                        "• If Battery is plugged in\n"
                                        "• Battery remianing time\n"
                                        "• List of names of users", font=("Times New Roman", 12))
    information_info.grid(row=2, column=2)


root = Tk()
root.title("Text editor")
root.geometry('800x300')

chkValue = BooleanVar()
chkValue.set(False)

title = Label(text="System Analytics Tool", font=("Roboto", 20))
title.grid(row=0, column=1)

chkVerify = Checkbutton(root, text='I understand the information \nthat is being collected \nand I agree to the LICENSE.',
                        font=("Roboto", 12), var=chkValue, command=update)
chkVerify.grid(row=1, column=2)

collect_button = Button(root, text="Analyse!", font=("Roboto", 12), command=collect_info, state="disabled")
collect_button.grid(row=1, column=1)

information_button = Button(root, text="More Information", font=("Roboto", 12), command=get_info)
information_button.grid(row=1, column=0)

root.mainloop()
