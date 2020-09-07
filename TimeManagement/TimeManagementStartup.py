from datetime import datetime
import csv
import os
import TimeManagementResources as src

now = datetime.now()

if not os.path.isfile(src.path):
    print("Found no file")
    header = ['WeekNum', 'Date', 'DayOfWeek', 'StartTime', 'EndTime', 'TimeToday', 'TimeMonth']
    try:
        with open(src.path, 'w+', newline='\n') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(header)
            f.close()
    except IOError:
        print("Could not open file")


data = list(csv.reader(open(src.path), delimiter=';'))
lastLineDate = datetime.strptime(data[-1][1],'%Y-%m-%d')
if lastLineDate.date() == now.date():
    exit()


#Write initial info to file to save 'now'
row = [now.strftime("%V"), now.date(), src.weekDay(now.weekday()), now.time().strftime('%H:%M:%S'), '-', '-', '-']
print(row)
with open(src.path, 'a+', newline='\n') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(row)
    f.close()