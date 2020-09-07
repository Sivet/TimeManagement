from datetime import datetime
import os

# only works on windows, change if for linux
path = os.path.join('C:/Users', os.getlogin(), 'Documents/' + os.getlogin() + datetime.now().strftime('%Y%b') + '.csv')


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

