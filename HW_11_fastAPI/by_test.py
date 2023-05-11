from datetime import datetime, timedelta

date_now = datetime.now().date()
a = datetime.now().date() - timedelta(weeks=1)
d = a.replace(year=date_now.year)
f = datetime.strptime("1984-11-25", "%Y-%m-%d").date()
print(f, type(f))
