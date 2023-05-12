from fastapi import APIRouter, Depends, status, Query, Path, HTTPException
from sqlalchemy.orm import Session

from schemas import ContactModel, ContactResponse
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


@router.get("/", response_model=list[ContactResponse], dependencies=[Depends(access_get)])
async def get_contacts(limit: int = Query(10, le=300), offset: int = 0, db: Session = Depends(get_db),
                       _: User = Depends(auth_service.get_current_user)):
    contacts = await rep_contacts.get_contacts(limit, offset, db)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(access_get)])
async def get_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db),
                      _: User = Depends(auth_service.get_current_user)):
    contact = await rep_contacts.get_contact_id(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.get("/birthday_contacts/", response_model=list[ContactResponse], dependencies=[Depends(access_get)])
async def get_contacts_birthday(day_to_birthday: int = 7, db: Session = Depends(get_db),
                                _: User = Depends(auth_service.get_current_user)):
    contacts = await rep_contacts.get_birthday_contacts(day_to_birthday, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='birthdays of contacts not found!')
    return contacts


@router.get("/search/", response_model=list[ContactResponse], dependencies=[Depends(access_get)])
async def search(first_name: str | None = None,
                 last_name: str | None = None, email: str | None = None, db: Session = Depends(get_db),
                 _: User = Depends(auth_service.get_current_user)):
    contacts = await rep_contacts.get_search_contacts(first_name, last_name, email, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contacts not found!')
    return contacts


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(access_create)])
async def create_contact(body: ContactModel, db: Session = Depends(get_db),
                         _: User = Depends(auth_service.get_current_user)):
    contact = await rep_contacts.create(body, db)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(access_update)])
async def update_contact(body: ContactModel, contact_id: int = Path(ge=1), db: Session = Depends(get_db),
                         _: User = Depends(auth_service.get_current_user)):
    contact = await rep_contacts.update(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(access_delete)])
async def delete_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db),
                         _: User = Depends(auth_service.get_current_user)):
    contact = await rep_contacts.remove(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact
