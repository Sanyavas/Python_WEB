from datetime import datetime
from random import randint, choice

from faker import Faker
from sqlalchemy import select

from aux_functions import normalize_phone, get_list_of_date
from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session


'''Функція генерації фейкових даних та заповнення ними БД'''


def fill_data():
    # Не всі дані будуть динамічні. Створюємо списки предметів та груп
    disciplines = [
        "Python Core",
        "Soft-skills",
        "HTML/CSS",
        "Python WEB",
        "English",
        "Python for Data Science"
    ]

    groups = ["PG-8", "PG-9", "PG-10"]

    fake = Faker('uk-UA')
    number_of_teachers = 5
    number_of_students = 50

    def seed_teachers():
        for _ in range(number_of_teachers):

            teacher = Teacher(fullname=fake.name(),
                              phone=normalize_phone(fake.phone_number()),
                              address=fake.address())
            session.add(teacher)
        session.commit()

    def seed_disciplines():
        teacher_ids = session.scalars(select(Teacher.id)).all()
        for discipline in disciplines:
            session.add(Discipline(name=discipline, teacher_id=choice(teacher_ids)))
        session.commit()

    def seed_groups():
        for group in groups:
            session.add(Group(name=group))
        session.commit()

    def seed_students():
        group_ids = session.scalars(select(Group.id)).all()
        for _ in range(number_of_students):
            student = Student(fullname=fake.name(),
                              group_id=choice(group_ids),
                              phone=normalize_phone(fake.phone_number()),
                              email=fake.email())
            session.add(student)
        session.commit()

    def seed_grades():
        # дата початку навчального процесу
        start_date = datetime.strptime("2020-09-01", "%Y-%m-%d")
        # дата закінчення навчального процесу
        end_date = datetime.strptime("2021-05-25", "%Y-%m-%d")
        d_range = get_list_of_date(start_date, end_date)
        discipline_ids = session.scalars(select(Discipline.id)).all()
        student_ids = session.scalars(select(Student.id)).all()

        for d in d_range:  # пройдемось по кожній даті
            random_id_discipline = choice(discipline_ids)
            random_ids_student = [choice(student_ids) for _ in range(5)]
            # проходимося за списком "везучих" студентів, додаємо їх до списку
            # та генеруємо оцінку
            for student_id in random_ids_student:
                grade = Grade(grade=randint(1, 12), date_of=d, student_id=student_id,
                              discipline_id=random_id_discipline)
                session.add(grade)
        session.commit()

    seed_teachers()
    seed_disciplines()
    seed_groups()
    seed_students()
    seed_grades()


if __name__ == '__main__':
    fill_data()
