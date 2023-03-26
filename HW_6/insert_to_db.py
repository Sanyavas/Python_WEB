from random import randint
from datetime import datetime

from faker import Faker

from aux_functions import get_list_of_date, normalize_phone
from connection import create_connection

fake = Faker('uk-UA')


disciplines = [
    "Python Core",
    "Soft-skills",
    "HTML/CSS",
    "Python WEB",
    "English",
    "Python for Data Science"
]

groups = ["PG-8", "PG-9", "PG-10"]

NUMBERS_TEACHERS = 5
NUMBER_STUDENTS = 50


def seed_teacher(cursor):
    sql_ex = "INSERT INTO teachers(fullname, phone, address) VALUES(%s, %s, %s);"
    teachers = [fake.name() for _ in range(NUMBERS_TEACHERS)]
    phones = [normalize_phone(fake.phone_number()) for _ in range(NUMBERS_TEACHERS)]
    address = [fake.address() for _ in range(NUMBERS_TEACHERS)]
    cursor.executemany(sql_ex, zip(teachers, phones, address))


def seed_groups(cursor):
    sql_ex = "INSERT INTO groups(name) VALUES(%s);"
    cursor.executemany(sql_ex, zip(groups, ))


def seed_disciplines(cursor):
    sql_ex = "INSERT INTO disciplines(name, teacher_id) VALUES(%s, %s);"
    list_teacher_id = [randint(1, NUMBERS_TEACHERS) for _ in range(len(disciplines))]
    cursor.executemany(sql_ex, zip(disciplines, iter(list_teacher_id)))


def seed_students(cursor):
    sql_ex = "INSERT INTO students(fullname, group_id, email, phone, age) VALUES(%s, %s, %s, %s, %s);"
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    email = [fake.email() for _ in range(NUMBER_STUDENTS)]
    phone = [normalize_phone(fake.phone_number()) for _ in range(NUMBER_STUDENTS)]
    age = [randint(18, 80) for _ in range(NUMBER_STUDENTS)]
    list_group_id = [randint(1, len(groups)) for _ in range(NUMBER_STUDENTS)]
    cursor.executemany(sql_ex, zip(students, iter(list_group_id), email, phone, age))


def seed_grades(cursor):
    sql_ex = "INSERT INTO grades(student_id, discipline_id, grade, date_of) VALUES(%s, %s, %s, %s);"
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-30", "%Y-%m-%d")
    list_dates = get_list_of_date(start_date, end_date)
    grades = []

    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(5)]
        for student in random_students:
            grades.append((student, random_discipline, randint(4, 12), day.date()))
    cursor.executemany(sql_ex, grades)


if __name__ == '__main__':
    with create_connection() as connect:
        c = connect.cursor()

        seed_groups(c)
        seed_teacher(c)
        seed_disciplines(c)
        seed_students(c)
        seed_grades(c)
        connect.commit()

        print(f'[INFO] Add data in tables postgreSQL')
        print(f'[INFO] postgreSQL connecting closed')
