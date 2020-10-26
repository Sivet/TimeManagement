from datetime import datetime, timedelta
import csv
import TimeManagementResources as src

print('path:' + src.path)

def timeToday(startTime):
    h, m, s = startTime.split(':')
    return endTime - timedelta(hours=int(h), minutes=int(m), seconds=float(s))


def monthTotal():
    totalTime = timedelta()
    dataIter = iter(data)
    next(dataIter)
    for line in dataIter:
        h, m, s = line[5].split(':')
        totalTime += timedelta(hours=int(h), minutes=int(m), seconds=float(s))
    return totalTime


data = list(csv.reader(open(src.path), delimiter=';'))

endTime = datetime.now()
data[-1][4] = endTime.time().strftime('%H:%M:%S')
data[-1][5] = timeToday(data[-1][3]).strftime('%H:%M:%S')
data[-1][6] = src.hourBasedTime(monthTotal())

with open(src.path, 'w+', newline='\n') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(data)
