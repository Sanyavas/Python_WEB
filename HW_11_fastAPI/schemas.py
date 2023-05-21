from datetime import datetime, date
from pydantic import BaseModel, Field, EmailStr, validator

from normalize_number import normalize_phone
from src.database.models import Role


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


class UserModel(BaseModel):
    username: str = Field(min_length=3, max_length=15)
    email: EmailStr
    password: str = Field(min_length=4, max_length=15)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    avatar: str
    role: Role

    class Config:
        orm_mode = True


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RequestEmail(BaseModel):
    email: EmailStr
