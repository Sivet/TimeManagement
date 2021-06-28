from datetime import datetime, timedelta
import csv
import TimeManagementResources as src

print('path:' + src.path)

def timeToday(startTime, breakTime):
    startH, startM, startS = startTime.split(':')
    breakH, breakM, breakS = breakTime.split(':')
    return (endTime - timedelta(hours=int(startH), minutes=int(startM), seconds=float(startS))) - timedelta(hours=int(breakH), minutes=int(breakM), seconds=float(breakS))


def monthTotal():
    totalTime = timedelta()
    dataIter = iter(data)
    next(dataIter)
    for line in dataIter:
        h, m, s = line[5].split(':')
        totalTime += timedelta(hours=int(h), minutes=int(m), seconds=float(s))
    return totalTime


data = list(csv.reader(open(src.path), delimiter=src.delimiter))

endTime = datetime.now()
data[-1][4] = endTime.time().strftime('%H:%M:%S')
data[-1][6] = timeToday(data[-1][3], data[-1][5]).strftime('%H:%M:%S')
#data[-1][7] = src.hourBasedTime(monthTotal())

with open(src.path, 'w+', newline='\n') as f:
    writer = csv.writer(f, delimiter=src.delimiter)
    writer.writerows(data)
