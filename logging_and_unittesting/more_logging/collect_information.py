import logging
import os
import psutil
from datetime import datetime
import time

logging.basicConfig(filename='system_info.log', level=logging.DEBUG)


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def getmessage(message):
    print(message)
    return " {date}; {username}; {message}".format(date=datetime.today().strftime('%Y-%m-%d'),
                                                   username=os.getlogin(), message=message)


logging.info(getmessage("Logging Session has begun"))

try:
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
except Exception as e:
    logging.error(getmessage("Exception Occurred: '{e}'".format(e=e)))
    print("There seems to be an error...")
    time.sleep(3)

logging.info(getmessage("Logging Session has ended"))
time.sleep(3)
