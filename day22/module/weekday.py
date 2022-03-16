import datetime

days = ['월', '화', '수', '목', '금', '토', '일']

now = datetime.datetime.today()
print(now)
print("{}년".format(now.year))
print()

weekday = datetime.datetime.today().weekday()
print(weekday)
print("{}요일".format(days[weekday]))

theday = datetime.datetime(2022, 3, 13).weekday()
print(theday)
print(days[theday])
