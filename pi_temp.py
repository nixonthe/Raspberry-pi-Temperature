#! /usr/bin/python3

from gpiozero import CPUTemperature
import datetime
import time

# замер температуры
def temp():
    t = CPUTemperature()
    return "Current temperature is: {}".format(t.temperature)

# дата при записи в файл
def date_time():
    dateandtime = datetime.datetime.now()
    date = dateandtime.strftime("%Y.%m.%d")
    time = dateandtime.strftime("%H:%M:%S")
    return "Date: {}; Time: {}".format(date, time)


name = str(input("Enter file's name: "))
def save(func1, func2):
    with open(name, "a") as f:
        f.write("{} -- {}\n".format(func1, func2))
        return

# вывод
count = int(input("How many values need: "))
count *= 10
period = int(input("Enter period in sec: "))
while count > 0:
    save(temp(), date_time())
    time.sleep(period)
    count -= 10

print("Finished!")
