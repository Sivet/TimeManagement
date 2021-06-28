from datetime import datetime
import csv
import os
import TimeManagementResources as src

now = datetime.now()

#print('path:' + src.path)

def writeInitTime(writer):
    row = [now.strftime("%V"), now.date(), src.weekDay(now.weekday()), now.time().strftime('%H:%M:%S'), '-', '0:0:0', '-']#, '-']
    print(row)
    writer.writerow(row)

if not os.path.isfile(src.path):
    print("Found no file")
    header = ['WeekNum', 'Date', 'DayOfWeek', 'StartTime', 'EndTime', 'BreakTime', 'TimeToday']#, 'TimeMonth']
    try:
        with open(src.path, 'w+', newline='\n') as f:
            writer = csv.writer(f, delimiter=src.delimiter)
            writer.writerow(header)
            writeInitTime(writer)
            f.close()
            exit()
    except IOError:
        print("Could not open file")


data = list(csv.reader(open(src.path), delimiter=src.delimiter))
#print(len(data[-1]))
lastLineDate = datetime.strptime(data[-1][1],'%Y-%m-%d')
if lastLineDate.date() == now.date():
    exit()


# Write initial info to file to save 'now'
with open(src.path, 'a+', newline='\n') as f:
        writer = csv.writer(f, delimiter=src.delimiter)
        writeInitTime(writer)
        f.close()
