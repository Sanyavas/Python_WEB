from datetime import datetime, date, timedelta


def user_digit():
    while True:
        day = input(">>> ")
        if not day.isdigit() or int(day) < 1:
            print(f"Введіть цифру від 1 до 10")
            continue
        elif int(day) > 10:
            print(f"Я вивожу курс валют за останні 10 днів! ")
            continue
        else:
            return day


def main():
    a = []
    now_date = date.today()
    cor_day = user_digit()
    for i in range(int(cor_day)):
        interval = timedelta(days=i)
        st = (now_date - interval).strftime('%d.%m.%Y')
        a.append(st)

    return a


if __name__ == '__main__':

    print(main())
