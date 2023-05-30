import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from src.schemas import ContactModel
from src.database.models import Contact
from src.repository.contacts import (
    get_contacts,
    get_contact_id,
    get_birthday_contacts,
    get_search_contacts,
    create,
    update,
    remove,
)


class TestContacts(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        # Create a mock session for testing
        self.db = MagicMock(spec=Session)

    async def test_get_contacts(self):
        # Mock the query method of the session to return a list of contacts
        contacts = [Contact() for _ in range(5)]
        self.db.query(Contact).limit().offset().all.return_value = contacts
        result = await get_contacts(limit=10, offset=0, db=self.db)
        self.assertEqual(result, contacts)

    async def test_get_contact_id(self):
        self.db.query.return_value.filter.return_value.first.return_value = Contact(id=1, first_name='John',
                                                                                    last_name='Doe',
                                                                                    email='john@example.com',
                                                                                    phone=+380123456789,
                                                                                    birthday='1990-05-27')
        contact = await get_contact_id(contact_id=1, db=self.db)
        self.assertEqual(contact.first_name, 'John')

    async def test_get_birthday_contacts(self):
        # Mock the query method of the session to return a list of contacts
        self.db.query.return_value.all.return_value = [
            Contact(id=1, first_name='John', last_name='Doe', email='john@example.com', phone=+380123456789,
                    birthday='1990-06-03'),
            Contact(id=2, first_name='Jane', last_name='Smith', email='jane@example.com', phone=+380987654321,
                    birthday='1995-08-10')
        ]
        contacts = await get_birthday_contacts(b_days=7, db=self.db)
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0].first_name, 'John')

    async def test_get_search_contacts(self):
        # Create mock contacts
        contacts = [
            Contact(id=1, first_name='John', last_name='Doe', email='john@example.com', phone='+380123456789',
                    birthday='1990-05-27'),
            Contact(id=2, first_name='Jane', last_name='Smith', email='jane@example.com', phone='+380987654321',
                    birthday='1995-08-10')
        ]

        # Mock the query method of the session to return the list of contacts
        self.db.query.return_value.filter.return_value.all.return_value = contacts

        # Call the function under test
        search_result = await get_search_contacts(first_name='John', last_name='Doe', email='john@example.com',
                                                  db=self.db)

        # Assert that the result matches the expected contacts
        self.assertEqual(search_result, contacts)

    async def test_create(self):
        contact_data = ContactModel(first_name='John', last_name='Doe', email='john@example.com', phone='+380123456789',
                                    birthday='1990-05-27')
        contact = await create(body=contact_data, db=self.db)  # Use 'await' to get the result from the coroutine
        self.assertEqual(contact.first_name, 'John')

    async def test_update(self):
        self.db.query.return_value.filter.return_value.first.return_value = Contact(id=1, first_name='John',
                                                                                    last_name='Doe',
                                                                                    email='john@example.com',
                                                                                    phone=+380123456789,
                                                                                    birthday='1990-05-27')
        contact_data = ContactModel(first_name='John', last_name='Smith', email='john@example.com',
                                    phone='+380123456789', birthday='1990-05-27')
        contact = await update(contact_id=1, body=contact_data, db=self.db)
        self.assertEqual(contact.last_name, 'Smith')

    async def test_remove(self):
        self.db.query.return_value.filter.return_value.first.return_value = Contact(id=1, first_name='John',
                                                                                    last_name='Doe',
                                                                                    email='john@example.com',
                                                                                    phone=+380123456789,
                                                                                    birthday='1990-05-27')
        contact = await remove(contact_id=1, db=self.db)
        self.assertEqual(contact.first_name, 'John')

