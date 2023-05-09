import re
from datetime import datetime, date
from pydantic import BaseModel, Field, EmailStr, validator

from normalize_number import normalize_phone


class ContactModel(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    email: EmailStr
    phone: str = Field(example="0672553355")
    birthday: date

    @validator("phone")
    def phone_number(cls, v):
        fix_phone = normalize_phone(v)
        if fix_phone is None:
            raise ValueError("Format phone number: '0502586987'")
        return fix_phone


class ContactResponse(ContactModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
