import datetime

#1
cur_d = datetime.datetime.now()
x = cur_d - datetime.timedelta(days=5)
print(x)

#2
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorow = today + datetime.timedelta(days=1)
print(f"yesterday: {yesterday}\ntoday: {today}\ntommorow: {tomorow}")

#3
cur_d = datetime.datetime.now()
cur_d_without_microsec = cur_d.replace(microsecond=0)
print(f"datetime without microseconds: {cur_d_without_microsec}")

#4
difference = (today-yesterday).total_seconds()
print(difference)