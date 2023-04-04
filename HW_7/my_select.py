from sqlalchemy import func, desc, select, and_

from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session


def select_1():
    """
-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT s.fullname as student, ROUND(avg(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 5;
    """
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade")) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc("avg_grade")).limit(5).all()
    return result


def select_2():
    """
-- Знайти студента із найвищим середнім балом з певного предмета.

SELECT d.name as discipline, s.fullname as student, ROUND(avg(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
WHERE d.id IN (1)
GROUP BY s.id, d.id
ORDER BY avg_grade DESC
LIMIT 1;
    """
    result = session.query(Discipline.name, Student.fullname,
                           func.round(func.avg(Grade.grade), 2).label("avg_grade")) \
        .select_from(Grade).join(Student).join(Discipline).filter(Discipline.id == 5) \
        .group_by(Student.id).group_by(Discipline.id).order_by(desc("avg_grade")).limit(5).first()
    return result


def select_3():
    """
-- Знайти середній бал у групах з певного предмета.

SELECT gr.name as group, d.name as discipline , ROUND(avg(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
left join "groups" gr on gr.id = s.group_id
WHERE d.id = 1
GROUP BY gr.id, d.id
ORDER BY avg_grade DESC
    """
    result = session.query(Group.name, Discipline.name, func.round(func.avg(Grade.grade), 2).label("avg_grade")) \
        .select_from(Grade).join(Student).join(Discipline).join(Group).filter(Discipline.id == 2) \
        .group_by(Discipline.id).group_by(Group.id).order_by(desc("avg_grade")).all()
    return result


def select_4():
    """
-- Знайти середній бал на потоці (по всій таблиці оцінок).

SELECT ROUND(AVG(g.grade), 2) AS all_avg_grade
FROM grades g;
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade")).select_from(Grade).all()
    return result


def select_5():
    """
-- Знайти які курси читає певний викладач.

SELECT t.fullname as teacher, d.name as discipline
FROM disciplines d
left join teachers t on t.id = d.teacher_id
where t.id = 2
GROUP BY t.id, d.id;
    """
    result = session.query(Teacher.fullname, Discipline.name).select_from(Discipline).join(Teacher) \
        .filter(Teacher.id == 3).group_by(Teacher.id).group_by(Discipline.id).all()
    return result


def select_6():
    """
-- Знайти список студентів у певній групі.

SELECT s.fullname AS student, g.name AS group
FROM students s
LEFT JOIN groups g ON g.id = s.group_id
WHERE g.id = 3
ORDER BY s.fullname;
    """
    result = session.query(Student.fullname, Group.name).select_from(Student).join(Group) \
        .filter(Group.id == 1).all()
    return result


def select_7():
    """
-- Знайти оцінки студентів у окремій групі з певного предмета.

SELECT s.fullname AS student, g.name AS group, g2.grade, d."name" as discipline
FROM students s
left join grades g2 on g2.student_id = g2.grade
LEFT JOIN groups g ON g.id = s.group_id
left join disciplines d on d.id = g2.discipline_id
WHERE g.id = 1 and d.id = 4
ORDER BY s.fullname;
    """
    result = session.query(Student.fullname, Group.name, Grade.grade, Discipline.name) \
        .select_from(Student).join(Grade).join(Group).join(Discipline) \
        .filter(Group.id == 1).filter(Discipline.id == 4).order_by(Student.fullname).all()
    return result


def select_8():
    """
-- Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT t.fullname as teacher, d."name" as discipline, ROUND(avg(g.grade), 2) as avg_grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
left join teachers t on t.id = d.teacher_id
WHERE t.id = 5
GROUP BY t.id, d.id;
    """
    result = session.query(Teacher.fullname, Discipline.name,
                           func.round(func.avg(Grade.grade), 2).label("avg_grade")) \
        .select_from(Grade).join(Discipline).join(Teacher).filter(Teacher.id == 4) \
        .group_by(Teacher.id).group_by(Discipline.id).all()
    return result


def select_9():
    """
-- Знайти список курсів, які відвідує студент.

SELECT s.fullname as student, d."name" as discipline
FROM grades g
join disciplines d on d.id = g.discipline_id
left join students s  on s.id = g.student_id
where s.id = 2
GROUP BY s.id, d.id
    """
    result = session.query(Student.fullname, Discipline.name).select_from(Grade).join(Discipline).join(Student) \
        .filter(Student.id == 4).group_by(Student.id).group_by(Discipline.id).all()
    return result


def select_10():
    """
-- Список курсів, які певному студенту читає певний викладач.

SELECT s.fullname AS student, t.fullname as teacher, d."name" as discipline
FROM grades g
left join disciplines d  on d.id = g.discipline_id
left join students s on s.id = g.student_id
LEFT JOIN teachers t on t.id = d.teacher_id
WHERE s.id = 2 and t.id = 1
GROUP BY d."name", t.fullname, s.fullname;

    """
    result = session.query(Student.fullname, Discipline.name, Teacher.fullname).select_from(Grade) \
        .join(Discipline).join(Student).join(Teacher).filter(Student.id == 4).filter(Teacher.id == 4) \
        .group_by(Student.id).group_by(Discipline.id).group_by(Teacher.id).all()
    return result


def select_11():
    """
-- Середній бал, який певний викладач ставить певному студентові.

SELECT t.fullname as teacher, s.fullname AS student, d."name" as discipline, ROUND(avg(g.grade), 2) as avg_grade
FROM grades g
left join disciplines d  on d.id = g.discipline_id
left join students s on s.id = g.student_id
LEFT JOIN teachers t on t.id = d.teacher_id
LEFT JOIN grades g2 on g2.student_id = g2.discipline_id
WHERE s.id = 5 and t.id = 2
GROUP BY t.fullname, s.fullname, d."name"
ORDER BY avg_grade DESC;
    """
    result = session.query(Teacher.fullname, Discipline.name, Student.fullname,
                           func.round(func.avg(Grade.grade), 2).label("avg_grade")) \
        .select_from(Grade).join(Discipline).join(Student).join(Teacher) \
        .filter(Student.id == 5).filter(Teacher.id == 3) \
        .group_by(Teacher.id).group_by(Student.id).group_by(Discipline.id).order_by(desc("avg_grade")).all()
    return result


def select_12():
    """
-- Оцінки студентів у певній групі з певного предмета на останньому занятті.

SELECT gr.name AS group, d."name" as discipline, s.fullname AS student, max(g.date_of) as max_date, g.grade
FROM grades g
join disciplines d  on d.id = g.discipline_id
join students s on s.id = g.student_id
JOIN "groups" gr on gr.id = s.group_id
WHERE gr.id = 2 and d.id = 3
and g.date_of =(
                SELECT MAX(date_of) FROM grades g2
                JOIN students s2 ON s2.id = g2.student_id
                WHERE g2.discipline_id = 2 AND gr2.id = 3
                )
    """
    subquery = (select(func.max(Grade.date_of)).join(Student).filter(and_(
        Grade.discipline_id == 2, Student.group_id == 3)).scalar_subquery())

    result = session.query(Group.name, Discipline.name, Grade.grade, Student.fullname, Grade.date_of) \
        .select_from(Grade).join(Student).join(Group).join(Discipline) \
        .filter(and_(Grade.discipline_id == 2, Student.group_id == 3, Grade.date_of == subquery)).all()
    return result


def main(num):
    if num == "1":
        print(select_1())
    elif num == "2":
        print(select_2())
    elif num == "3":
        print(select_3())
    elif num == "4":
        print(select_4())
    elif num == "5":
        print(select_5())
    elif num == "6":
        print(select_6())
    elif num == "7":
        print(select_7())
    elif num == "8":
        print(select_8())
    elif num == "9":
        print(select_9())
    elif num == "10":
        print(select_10())
    elif num == "11":
        print(select_11())
    elif num == "12":
        print(select_12())
    else:
        print(f'Not found Query!!')
