from datetime import datetime, timedelta
import csv
import os

now = datetime.now()
path = os.path.join('C:/Users', os.getlogin(), 'Documents/TimeManagement.csv') #only works on windows, change if for linux


def weekDay(day):
    switcher = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return switcher.get(day)


def weekTotal(Timetoday):
    totalTime = Timetoday
    with open(path, newline='\n') as file:
        lines = file.readlines()
    file.close()
    del lines[0]
    if not lines:
        return abs(totalTime)
    lines.reverse()
    for line in lines:
        if line != '\r\n':
            split = line.split(',')
            if split[3] != now.strftime("%V"):
                return abs(totalTime)
            h, m, s = split[1].split(':')
            totalTime += timedelta(hours=int(h), minutes=int(m), seconds=float(s))
    return abs(totalTime)


def calcTime():
    new = datetime.now()
    if not os.path.isfile(path):
        header = ['Date', 'TimeToday', 'DayOfWeek', 'WeekNum', 'TotalTimeWeek']
        with open(path, 'w+', newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            f.close()
    row = [now.date(), new - now, weekDay(now.weekday()), now.strftime("%V"), weekTotal(new - now)]
    print(row)
    with open(path, 'a+', newline='\n') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()


while True:
    k = input()
    if k == "exit":
        calcTime()
        print("Shutting down")
        #os.system("shutdown /s /t 1") #only works on windows, change if for linux
        break
    elif k == "today":
        new = datetime.now()
        print("Time today so far ", new - now)
    elif k == "week":
        new = datetime.now()
        print("Time this week so far ", weekTotal(new - now))
    else:
        print("Not a valid command")
        print("Valid commands are:\n - exit - to shutdown\n - today - for today's time\n - week - for week's total time")