from datetime import datetime
import csv
import os

now = datetime.now()
path = os.path.join('C:/Users', os.getlogin(), 'Documents/TimeManagement.csv') #only works on windows, change if for linux


def calcTime():
    new = datetime.now()
    row = [now.date(), new - now]
    with open(path, 'a', newline='\n') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    csvFile.close()


while True:
    k = input()
    if(k == "exit"):
        calcTime()
        os.system("shutdown /s /t 1")
    print("Type exit to shutdown")