from datetime import datetime, timedelta, date

date_now = datetime.now().date()
a = datetime.now().date() - timedelta(weeks=1)
d = a.replace(year=date_now.year)
f = datetime.strptime("1984-11-25", "%Y-%m-%d").date()
print(f, type(f))
b_days = 180

contacts = ["1984-11-25", "1984-01-25", "1984-02-25", "1984-08-25", "1984-06-25", "1984-07-25", ]

list_contacts = []
for contact in contacts:
    datatime_birthday = datetime.strptime(contact, "%Y-%m-%d").date()
    cor_contact_year = datatime_birthday.replace(year=date_now.year)
    if date_now + timedelta(b_days) >= cor_contact_year > date_now:
        list_contacts.append(contact)
print(list_contacts)
