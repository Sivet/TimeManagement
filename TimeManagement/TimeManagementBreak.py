from datetime import datetime, timedelta
import csv
import TimeManagementResources as src

def breakTime(currentBreak):
    h, m, s = currentBreak.split(':')
    return newBreak + timedelta(hours=int(h), minutes=int(m), seconds=float(s))


startBreak = datetime.now()
print("Break started, type \"Done\" to end")
while True:
    value = input()

    if value == "Done":
        newBreak = datetime.now() - startBreak
        data = list(csv.reader(open(src.path), delimiter=src.delimiter))
        data[-1][5] = src.hourBasedTime(breakTime(data[-1][5]))
        break
    else:
        print("Command not recognized")

with open(src.path, 'w+', newline='\n') as f:
    writer = csv.writer(f, delimiter=src.delimiter)
    writer.writerows(data)