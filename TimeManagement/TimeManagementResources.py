from datetime import datetime
import os


if(os.name == 'nt'):
    path = os.path.join('C:/Users', os.getlogin(), 'Documents/TimeManagement/' + os.getlogin() + datetime.now().strftime('%Y%b') + '.csv') #Windows
else:
    path = os.path.expanduser("~/Documents/TimeManagement/" + str(os.getlogin()) + datetime.now().strftime("%Y%b") + ".csv") #Linux

delimiter = ','

#str(os.getenv('LOGNAME'))
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


def hourBasedTime(time):
    seconds = time.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    string = '{}:{}:{}'.format(int(hours), int(minutes), int(seconds))
    return string
