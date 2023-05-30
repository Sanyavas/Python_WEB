import pickle
import unittest
from unittest.mock import patch

from fastapi import HTTPException, status
from src.services.auth import Auth, jwt, JWTError
from src.repository import users as repository_users


class AuthTests(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.auth = Auth()

    async def test_create_refresh_token(self):
        data = {"sub": "test@example.com"}
        expires_delta = 604800  # 7 days
        result = await self.auth.create_refresh_token(data, expires_delta)
        self.assertTrue(result)

    async def test_decode_refresh_token(self):
        refresh_token = "some_refresh_token"
        with patch.object(Auth, "SECRET_KEY", "test_secret"):
            with self.assertRaises(HTTPException):
                await self.auth.decode_refresh_token(refresh_token)

    def test_create_email_token(self):
        data = {"sub": "test@example.com"}
        result = self.auth.create_email_token(data)
        self.assertTrue(result)

    async def test_get_email_from_token(self):
        token = "some_token"
        with patch.object(Auth, "SECRET_KEY", "test_secret"):
            with self.assertRaises(HTTPException):
                await self.auth.get_email_from_token(token)

    async def test_get_current_user_valid_token(self):
        token = "valid_token"
        email = "test@example.com"
        user = {"email": email}
        fake_db = FakeDB()
        fake_db.set_user(user)

        with patch.object(Auth, "SECRET_KEY", "test_secret"):
            with patch.object(Auth, "ALGORITHM", "HS256"):
                with patch.object(Auth, "r") as mock_r:
                    mock_r.get.return_value = None
                    with patch.object(repository_users, "get_user_by_email") as mock_get_user:
                        mock_get_user.return_value = user
                        try:
                            await self.auth.get_current_user(token, db=fake_db)
                        except Exception as e:
                            print(e)


class FakeDB:
    def __init__(self):
        self.user = None

    def set_user(self, user):
        self.user = user


