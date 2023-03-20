from datetime import date, timedelta


def user_digit(user_input):
    """Перевіряє коректність вводу числа"""

    if not user_input.isdigit() or int(user_input) < 1:
        print(f"Entered {user_input} Enter digit: 1-10")
    elif int(user_input) > 10:
        print(f"Entered {user_input} Max 10 days! ")
    else:
        return user_input


def main(day):
    """Вертає список дат в строковому форматі"""

    list_dates = []
    now_date = date.today()
    cor_day = user_digit(day)
    for i in range(int(cor_day)):
        interval = timedelta(days=i)
        st = (now_date - interval).strftime('%d.%m.%Y')
        list_dates.append(st)
    return list_dates
