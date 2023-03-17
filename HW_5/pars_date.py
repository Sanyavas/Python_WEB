"""
Функція user_digit() приймає та перевіряє введене число, ф-я main() перетворює дати в строку та закидує дати у список
"""

from datetime import date, timedelta


def user_digit(day):

    if not day.isdigit() or int(day) < 1:
        print(f"Введіть цифру від 1 до 10")

    elif int(day) > 10:
        print(f"Я вивожу курс валют за останні 10 днів! ")

    else:
        return day


def main(day):
    a = []
    now_date = date.today()
    cor_day = user_digit(day)
    for i in range(int(cor_day)):
        interval = timedelta(days=i)
        st = (now_date - interval).strftime('%d.%m.%Y')
        a.append(st)

    return a


if __name__ == '__main__':
    print(main())
