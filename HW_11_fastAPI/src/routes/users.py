from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from src.schemas import UserResponse
from src.database.db import get_db
from src.database.models import User
from src.repository import users as repository_users
from src.services.auth import auth_service
from src.services.upload_avatar import UploadService


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me/", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(auth_service.get_current_user)):
    """
    The read_users_me function is a GET endpoint that returns the current user's information.

    :param current_user: User: Pass the current user to the function
    :return: The current user object
    """
    return current_user


@router.patch('/avatar', response_model=UserResponse)
async def update_avatar_user(avatar: UploadFile = File(), current_user: User = Depends(auth_service.get_current_user),
                             db: Session = Depends(get_db)):

    """
    The update_avatar_user function updates the avatar of a user.

    :param avatar: UploadFile: Receive the avatar file from the client
    :param current_user: User: Get the current user
    :param db: Session: Pass the database session to the function
    :return: The updated user
    """
    public_id = UploadService.create_name_avatar(current_user.email, '007')

    r = UploadService.upload(avatar.file, public_id)
    src_url = UploadService.get_url_avatar(public_id, r.get('version'))
    user = await repository_users.update_avatar(current_user.email, src_url, db)
    return user
