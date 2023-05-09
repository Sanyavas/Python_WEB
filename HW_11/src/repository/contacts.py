from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from schemas import ContactModel
from src.database.models import Contact


async def get_contacts(limit: int, offset: int, db: Session):
    contacts = db.query(Contact).limit(limit).offset(offset).all()
    return contacts


async def get_contact_id(contact_id: int, db: Session):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    return contact


async def get_birthday_contacts(b_days: int, db: Session):
    contacts = db.query(Contact).all()
    date_now = datetime.now().date()
    list_contacts = []
    for contact in contacts:
        datatime_birthday = datetime.strptime(contact.birthday, "%Y-%m-%d").date()
        cor_contact_year = datatime_birthday.replace(year=date_now.year)
        if date_now + timedelta(b_days) >= cor_contact_year > date_now:
            list_contacts.append(contact)
    return list_contacts


async def get_search_contacts(first_name: str, last_name: str, email: str, db: Session):
    contacts = db.query(Contact).filter((Contact.first_name.ilike(f"%{first_name}%")) |
                                        (Contact.last_name.ilike(f"%{last_name}%")) |
                                        (Contact.email.ilike(f"%{email}%"))).all()
    return contacts


async def create(body: ContactModel, db: Session):
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    return contact


async def update(contact_id: int, body: ContactModel, db: Session):
    contact = await get_contact_id(contact_id, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.phone = body.phone
        contact.email = body.email
        contact.birthday = body.birthday
        db.commit()
    return contact


async def remove(contact_id: int, db: Session):
    contact = await get_contact_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact
