import datetime

date = datetime.date(2026, 10, 24)
today = datetime.date.today()
now_datetime  = datetime.datetime.now()
now_datetime_string  = datetime.datetime.now().strftime("%H:%M:%S")
current_time = datetime.datetime.now().time()

take_time = input("Enter time: ")
print(current_time)