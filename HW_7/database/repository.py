

from sqlalchemy import and_, select

from aux_functions import normalize_phone
from database.db import session
from database.models import Teacher, Student, Discipline, Group, Grade


def create_data(my_model, my_argv: dict):
    data = None
    if my_model == Group:
        data = my_model(name=my_argv.get("name"))
    if my_model == Teacher:
        data = my_model(fullname=my_argv.get("name"),
                        phone=normalize_phone(my_argv.get("phone")),
                        email=my_argv.get("email"),
                        address=my_argv.get("address"))
    if my_model == Discipline:
        data = my_model(name=my_argv.get("name"),
                        teacher_id=my_argv.get("teacher_id"))
    if my_model == Student:
        data = my_model(fullname=my_argv.get("name"),
                        phone=normalize_phone(my_argv.get("phone")),
                        email=my_argv.get("email"),
                        group_id=my_argv.get("group_id"))
    if my_model == Grade:
        data = my_model(grade=my_argv.get("grade"),
                        date_of=my_argv.get("date_of"),
                        student_id=my_argv.get("student_id"),
                        discipline_id=my_argv.get("discipline_id"))
    session.add(data)
    session.commit()
    session.close()


def read_data(model):
    stmt = select('*').select_from(model)
    result = session.execute(stmt).fetchall()
    return result


def update_data(my_model, my_argv: dict):
    upd = session.query(my_model).filter(my_model.id == my_argv.get("id"))
    if upd:
        if my_model == Group:
            upd.name = my_argv.get("name") if my_argv.get("name") else my_model.name
            upd.update(upd.name)

        if my_model == Teacher:
            upd.fullname = my_argv.get("name") if my_argv.get("name") else my_model.fullname
            upd.phone = my_argv.get("phone") if my_argv.get("phone") else my_model.phone
            upd.email = my_argv.get("email") if my_argv.get("email") else my_model.email
            upd.address = my_argv.get("address") if my_argv.get("address") else my_model.address
            upd.update({"fullname": upd.fullname,
                        "phone": normalize_phone(upd.phone),
                        "email": upd.email,
                        "address": upd.address})

        if my_model == Discipline:
            upd.name = my_argv.get("name") if my_argv.get("name") else my_model.name
            upd.teacher_id = my_argv.get("teacher_id") if my_argv.get("teacher_id") else my_model.teacher_id
            upd.update({"name": upd.name,
                        "teacher_id": upd.teacher_id})
        if my_model == Student:
            upd.fullname = my_argv.get("name") if my_argv.get("name") else my_model.fullname
            upd.phone = my_argv.get("phone") if my_argv.get("phone") else my_model.phone
            upd.email = my_argv.get("email") if my_argv.get("email") else my_model.email
            upd.group_id = my_argv.get("group_id") if my_argv.get("group_id") else my_model.group_id
            upd.update({"fullname": upd.fullname,
                        "phone": normalize_phone(upd.phone),
                        "email": upd.email,
                        "group_id": upd.group_id})

        if my_model == Grade:
            upd.grade = my_argv.get("grade") if my_argv.get("grade") else my_model.grade
            upd.date_of = my_argv.get("date_of") if my_argv.get("date_of") else my_model.date_of
            upd.student_id = my_argv.get("student_id") if my_argv.get("student_id") else my_model.student_id
            upd.discipline_id = my_argv.get("discipline_id") if my_argv.get("discipline_id") else my_model.discipline_id
            upd.update({"grade": upd.grade,
                        "date_of": upd.date_of,
                        "student_id": upd.student_id,
                        "discipline_id": upd.discipline_id})
        session.commit()
        session.close()
        return upd.first()
    return upd


def delete_data(model, my_argv: dict):
    dd = session.query(model).filter(model.id == my_argv.get("id")).delete()
    session.commit()
    session.close()
    return dd
