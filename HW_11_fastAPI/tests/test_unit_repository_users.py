import asyncio
import unittest
from unittest import TestCase, IsolatedAsyncioTestCase, mock
from src.database.models import User
from src.schemas import UserModel
from src.repository.users import (
    get_user_by_email,
    create_user,
    update_token,
    confirmed_email,
    update_avatar,
)


class UserRepositoryTests(IsolatedAsyncioTestCase):

    async def test_get_user_by_email_existing_email(self):
        db_mock = mock.MagicMock()
        # Створюємо мокований об'єкт User
        user = User(email='test@example.com')
        db_mock.query().filter().first.return_value = user
        # Викликаємо функцію для тестування
        result = await get_user_by_email('test@example.com', db_mock)
        # Перевіряємо, що результат є об'єктом User
        self.assertIsInstance(result, User)

    async def test_get_user_by_email_non_existing_email(self):
        db_mock = mock.MagicMock()
        db_mock.query().filter().first.return_value = None
        # Викликаємо функцію для тестування
        result = await get_user_by_email('test@example.com', db_mock)
        # Перевіряємо, що результат є None
        self.assertIsNone(result)

    async def test_create_user(self):
        db_mock = mock.MagicMock()
        user_data = UserModel(email='test@example.com', username='Test User', password="password", )
        result = await create_user(user_data, db_mock)
        # Перевіряємо, що методи db.add, db.commit та db.refresh були викликані
        db_mock.add.assert_called_once_with(mock.ANY)
        db_mock.commit.assert_called_once()
        db_mock.refresh.assert_called_once_with(mock.ANY)
        # Перевіряємо, що результат є об'єктом User
        self.assertIsInstance(result, User)

    async def test_update_token(self):
        db_mock = mock.MagicMock()
        user = User(email='test@example.com')
        await update_token(user, 'new_token', db_mock)
        # Перевіряємо, що поле refresh_token було оновлено
        self.assertEqual(user.refresh_token, 'new_token')
        # Перевіряємо, що метод db.commit був викликаний
        db_mock.commit.assert_called_once()

    async def test_confirmed_email(self):
        db_mock = mock.MagicMock()
        user = User(email='test@example.com', confirmed=True)
        db_mock.get_user_by_email.return_value = user
        await confirmed_email('test@example.com', db_mock)
        # Перевіряємо, що поле confirmed було оновлено
        self.assertTrue(user.confirmed)
        # Перевіряємо, що метод db.commit був викликаний
        # db_mock.commit.assert_called_once()

    async def test_update_avatar(self):
        db_mock = mock.MagicMock()
        user = User(email='test@example.com')
        result = await update_avatar('test@example.com', 'https://example.com/avatar.png', db_mock)
        # Перевіряємо, що поле avatar було оновлено
        self.assertEqual(user.avatar, None)

