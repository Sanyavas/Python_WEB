from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from src.schemas import ContactModel
from src.database.models import Contact


async def get_contacts(limit: int, offset: int, db: Session):
    """
    The get_contacts function returns a list of contacts from the database.

    :param limit: int: Limit the number of contacts returned
    :param offset: int: Specify the number of records to skip before returning results
    :param db: Session: Pass the database session to the function
    :return: A list of contact objects
    """
    contacts = db.query(Contact).limit(limit).offset(offset).all()
    return contacts


async def get_contact_id(contact_id: int, db: Session):
    """
    The get_contact_id function takes in a contact_id and db Session object,
        queries the database for the contact with that id, and returns it.

    :param contact_id: int: Specify the id of the contact we want to retrieve
    :param db: Session: Pass the database session to the function
    :return: The contact object of the given id
    """
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    return contact


async def get_birthday_contacts(b_days: int, db: Session):
    """
    The get_birthday_contacts function returns a list of contacts whose birthday is within the next b_days days.

    :param b_days: int: Determine how many days in advance the user wants to be notified
    :param db: Session: Pass the database session to the function
    :return: A list of contacts whose birthday is within the next b_days days
    """
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
    """
    The get_search_contacts function searches the database for contacts that match the search criteria.
        The function takes in a first name, last name, and email address as parameters.
        It then uses SQLAlchemy to query the database for any contacts that have a matching first or last name or email address.
        If no matches are found, an empty list is returned.

    :param first_name: str: Filter the contacts by first name
    :param last_name: str: Filter the contacts by last name
    :param email: str: Search for contacts by email
    :param db: Session: Pass the database session object to the function
    :return: A list of contacts that match the search criteria
    """
    contacts = db.query(Contact).filter((Contact.first_name.ilike(f"%{first_name}%")) |
                                            (Contact.last_name.ilike(f"%{last_name}%")) |
                                            (Contact.email.ilike(f"%{email}%"))).all()
    return contacts


async def create(body: ContactModel, db: Session):
    """
    The create function creates a new contact in the database.

    :param body: ContactModel: Get the data from the request body
    :param db: Session: Connect to the database
    :return: A contact object
    """
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    return contact


async def update(contact_id: int, body: ContactModel, db: Session):
    """
    The update function updates a contact in the database.

    :param contact_id: int: Specify which contact to delete
    :param body: ContactModel: Update the contact with the new information
    :param db: Session: Pass the database session to the function
    :return: A contact object
    """
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
    """
    The remove function removes a contact from the database.

    :param contact_id: int: Specify the id of the contact to be deleted
    :param db: Session: Pass the database session to the function
    :return: The contact that was deleted
    """
    contact = await get_contact_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact
