import datetime
day1=datetime.date(2019,12,14)
day2=datetime.date(2021,6,5)
diff=day2-day1
print(diff.days)
print(day1.weekday())

today=datetime.date.today()
diff_days=datetime.timedelta(days=100)
print(today)
print(today+diff_days)