from fastapi import APIRouter, Depends, status, Query, Path, HTTPException
from sqlalchemy.orm import Session
from fastapi_limiter.depends import RateLimiter

from src.schemas import ContactModel, ContactResponse
from src.services.auth import auth_service
from src.database.db import get_db
from src.database.models import User, Role
from src.repository import contacts as rep_contacts
from src.services.roles import RolesAccess

router = APIRouter(prefix="/contacts", tags=["contacts"])

access_get = RolesAccess([Role.admin, Role.moderator, Role.user])
access_create = RolesAccess([Role.admin, Role.moderator])
access_update = RolesAccess([Role.admin, Role.moderator])
access_delete = RolesAccess([Role.admin])


@router.get("/", response_model=list[ContactResponse],
            dependencies=[Depends(access_get), Depends(RateLimiter(times=2, seconds=5))],
            description="Two request on 5 second")
async def get_contacts(limit: int = Query(10, le=300), offset: int = 0, db: Session = Depends(get_db)):
    """
    The get_contacts function returns a list of contacts.

    :param limit: int: Limit the number of contacts returned
    :param le: Limit the number of contacts returned
    :param offset: int: Specify the number of contacts to skip before returning
    :param db: Session: Get the database session
    :return: A list of contacts
    """
    contacts = await rep_contacts.get_contacts(limit, offset, db)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(access_get)])
async def get_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db),
                      _: User = Depends(auth_service.get_current_user)):
    """
    The get_contact function is used to retrieve a single contact from the database.
    It takes in an integer value for the contact_id, which is then passed into the get_contact_id function
    in rep_contacts.py, where it will be used to query for a specific contact in our database.

    :param contact_id: int: Get the contact_id from the url
    :param db: Session: Get the database session
    :param _: User: Ensure that the user is logged in
    :return: An instance of the contact model
    """
    contact = await rep_contacts.get_contact_id(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.get("/birthday_contacts/", response_model=list[ContactResponse], dependencies=[Depends(access_get)])
async def get_contacts_birthday(day_to_birthday: int = 7, db: Session = Depends(get_db),
                                _: User = Depends(auth_service.get_current_user)):
    """
    The get_contacts_birthday function returns a list of contacts that have their birthday in the next 7 days.
        The function takes an optional parameter day_to_birthday, which is set to 7 by default.
        If no contacts are found, it will return a 404 error.

    :param day_to_birthday: int: Get the contacts whose birthday is in 7 days
    :param db: Session: Get the database connection
    :param _: User: Get the current user
    :return: A list of contacts whose birthdays are within a certain number of days
    """
    contacts = await rep_contacts.get_birthday_contacts(day_to_birthday, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found!')
    return contacts


@router.get("/search/", response_model=list[ContactResponse], dependencies=[Depends(access_get)])
async def search(first_name: str | None = None,
                 last_name: str | None = None, email: str | None = None, db: Session = Depends(get_db),
                 _: User = Depends(auth_service.get_current_user)):
    """
    The search function allows the user to search for contacts by first name, last name, or email.
        The function takes in a first_name (str), last_name (str), and email (str) as parameters.
        It returns a list of contacts that match the search criteria.

    :param first_name: str | None: Specify the type of parameter that is expected
    :param last_name: str | None: Specify that the last_name parameter is optional
    :param email: str | None: Search for a contact by email
    :param db: Session: Get the database session
    :param _: User: Get the current user from the auth_service
    :return: A list of contacts
    """
    contacts = await rep_contacts.get_search_contacts(first_name, last_name, email, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found!')
    return contacts


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(access_create)])
async def create_contact(body: ContactModel, db: Session = Depends(get_db),
                         _: User = Depends(auth_service.get_current_user)):
    """
    The create_contact function creates a new contact in the database.

    :param body: ContactModel: Get the data from the request body
    :param db: Session: Pass the database session to the function
    :param _: User: Get the current user from the auth_service
    :return: The created contact
    """
    contact = await rep_contacts.create(body, db)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(access_update)])
async def update_contact(body: ContactModel, contact_id: int = Path(ge=1), db: Session = Depends(get_db),
                         _: User = Depends(auth_service.get_current_user)):
    """
    The update_contact function updates a contact in the database.
        The function takes an id and a body as parameters, which are used to update the contact.
        If no such contact exists, it returns 404 Not Found.

    :param body: ContactModel: Get the data from the request body
    :param contact_id: int: Get the contact id from the path
    :param db: Session: Get a database session
    :param _: User: Get the current user
    :return: The updated contact object
    """
    contact = await rep_contacts.update(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(access_delete)])
async def delete_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db),
                         _: User = Depends(auth_service.get_current_user)):
    """
    The delete_contact function deletes a contact from the database.
        It takes in an integer as a parameter, which is the ID of the contact to be deleted.
        The function returns a JSON object containing information about the deleted contact.

    :param contact_id: int: Get the id of the contact to be deleted
    :param db: Session: Get the database session
    :param _: User: Ensure that the user is authenticated
    :return: The deleted contact
    """
    contact = await rep_contacts.remove(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact
