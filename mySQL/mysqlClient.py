import mysql.connector
import psutil
import os
import time
from myInfo import getSQLPass

print("Attempting connection...")

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd=getSQLPass()
)

print("Connected successfully")
print(mysql)



mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS loggingInfo;")

mycursor.execute("USE loggingInfo")

mycursor.execute("CREATE TABLE IF NOT EXISTS log(user TINYTEXT, time DOUBLE, cpu FLOAT, ram FLOAT, battery TINYINT, batteryState TINYINT)")


userInput = input("To authorise this command, type 'banana' ")

if userInput == 'banana':
    logLoop = 1
    while logLoop == 1:
        user = os.getlogin()
        battery = psutil.sensors_battery()
        battPercent = battery.percent
        battState = battery.power_plugged
        if battState is True:
            battState = 1
        elif battState is False:
            battState = 0
        cpuUtilisation = psutil.cpu_percent(percpu=False)
        mem = psutil.virtual_memory()
        batt = psutil.sensors_battery()
        ramUtilisation = mem.percent
        currentTime = int(time.time())


        sqlFormula = "INSERT INTO log (user, time, cpu, ram, battery, batteryState) VALUES (%s, %s, %s, %s, %s, %s)"
        sqlInfo = (user, currentTime, cpuUtilisation, ramUtilisation, battPercent, battState)

        mycursor.execute(sqlFormula, sqlInfo)

        mydb.commit()

        print("Date sent!")
        print(sqlInfo)
        print("\n")

        time.sleep(1)
