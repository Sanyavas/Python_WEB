from datetime import timedelta
from prettytable import PrettyTable


def normalize_phone(value):
    new_value = (
        value.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    if new_value.isdigit():
        if len(new_value) == 12:
            new_value = "+" + new_value

        elif len(new_value) == 10:
            new_value = "+38" + new_value
        elif len(new_value) == 7:
            new_value = "+38044" + new_value

    return new_value


def get_list_of_date(start_date, end_date):
    result = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


def help_message():
    x = PrettyTable()
    x.field_names = ["№", "запит"]
    x.align = "l"
    x.add_rows(
        [
            ['33', 'ІНФО'],
            ['0', 'Вихід'],
            ['1', 'Знайти 5 студентів з найбільшим середнім балом по всім предметам'],
            ['2', 'Знайти студента з найбільшим середнім балом з дисципліни. (1-а дисципліна)'],
            ['3', 'Знайти середній бал в групі по дисципліні. (1-а дисципліна)'],
            ['4', 'Знайти середній бал на потоці (по всій таблиці grades)'],
            ['5', 'Які курси веде викладач. (1-й id=1)'],
            ['6', 'Список студентів в групі. (3-я група)'],
            ['7', 'Оцінки студентів в окремій групі(1-а група) за конкретною дисципліною(4-а дисципліна).'],
            ['8', 'Знайти середній бал, який ставить викладач по своїм дисциплінам. (1-й викладач)'],
            ['9', 'Знайти список курсів, які відвідує студент.'],
            ['10', 'Знайти список курсів, які конкретному студенту веде конкретний викладач.'],
            ['11', 'Середній бал, який конкретний викладач ставить конкретному студенту.'],
            ['12', 'Оцінки студентів в групі по дисципліні на останньому занятті.']
        ]
    )
    print("\nВиберіть який запит ви хочете виконати?")
    return x