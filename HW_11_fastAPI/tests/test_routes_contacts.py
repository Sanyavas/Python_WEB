from unittest.mock import MagicMock, patch, AsyncMock
from faker import Faker

import pytest

from src.database.models import User
from src.services.auth import auth_service

faker = Faker()

CONTACT = {
    "first_name": 'Bob',
    "last_name": 'Doe',
    "email": faker.email(),
    "phone": str(faker.msisdn()[:10]),
    "birthday": '1990-05-30'
}


@pytest.fixture()
def token(client, user, session, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
    client.post("/api/auth/signup", json=user)
    current_user: User = session.query(User).filter(User.email == user.get('email')).first()
    current_user.confirmed = True
    current_user.role = "admin"
    session.commit()
    response = client.post(
        "/api/auth/login",
        data={"username": user.get('email'), "password": user.get('password')},
    )
    data = response.json()
    return data["access_token"]


def test_create_contact(client, token):
    with patch.object(auth_service, "r") as redis_mock:
        redis_mock.get.return_value = None
        response = client.post("api/contacts", json=CONTACT, headers={"Authorization": f"Bearer {token}"})

        assert response.status_code == 201, response.text
        data = response.json()
        assert 'id' in data
        assert CONTACT["first_name"] == data["first_name"]


def test_get_contact(client, token, monkeypatch):
    with patch.object(auth_service, "r") as redis_mock:
        redis_mock.get.return_value = None
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.redis', AsyncMock())
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.identifier', AsyncMock())
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.http_callback', AsyncMock())
        response = client.get("api/contacts", headers={"Authorization": f"Bearer {token}"})

        assert response.status_code == 200, response.text
        data = response.json()
        assert 'id' in data[0]
        assert CONTACT["first_name"] == data[0]["first_name"]


def test_get_contact_id(client, token, monkeypatch):
    with patch.object(auth_service, "r") as redis_mock:
        redis_mock.get.return_value = None
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.redis', AsyncMock())
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.identifier', AsyncMock())
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.http_callback', AsyncMock())

        # Try to retrieve a nonexistent contact
        response = client.get("api/contacts/1", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200, response.text
        data = response.json()
        assert 'id' in data
        assert CONTACT["first_name"] == data["first_name"]


def test_get_not_contact_id(client, token, monkeypatch):
    with patch.object(auth_service, "r") as redis_mock:
        redis_mock.get.return_value = None
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.redis', AsyncMock())
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.identifier', AsyncMock())
        monkeypatch.setattr('fastapi_limiter.FastAPILimiter.http_callback', AsyncMock())

        # Try to retrieve a nonexistent contact
        response = client.get("api/contacts/999", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 404, response.text
        error = response.json()
        assert error["detail"] == "Not found!"


def test_search_contacts(client, token):
    with patch.object(auth_service, "r") as redis_mock:
        redis_mock.get.return_value = None
        query_params = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com"
        }
        response = client.get(
            "api/contacts/search/",
            headers={"Authorization": f"Bearer {token}"},
            params=query_params
        )

        assert response.status_code == 200, response.text
        data = response.json()
        assert isinstance(data, list)
        for contact in data:
            assert "id" in contact
            assert "first_name" in contact


def test_update_contact(client, token):
    with patch.object(auth_service, "r") as redis_mock:
        redis_mock.get.return_value = None
        contact_id = 1
        updated_contact_data = {
            "first_name": "Updated",
            "last_name": "Contact",
            "email": "updated@example.com",
            "phone": "+380987654321",
            "birthday": "1995-01-01"
        }
        response = client.put(
            f"api/contacts/{contact_id}",
            json=updated_contact_data,
            headers={"Authorization": f"Bearer {token}"}
        )

        assert response.status_code == 200, response.text
        data = response.json()
        assert "id" in data
        assert data["id"] == contact_id
        assert "first_name" in data
        assert data["first_name"] == updated_contact_data["first_name"]
        assert "last_name" in data
        assert data["last_name"] == updated_contact_data["last_name"]
        assert "email" in data
        assert data["email"] == updated_contact_data["email"]
        assert "phone" in data
        assert data["phone"] == updated_contact_data["phone"]
        assert "birthday" in data
        assert data["birthday"] == updated_contact_data["birthday"]
        # Perform additional assertions if needed


def test_delete_contact(client, token):
    with patch.object(auth_service, "r") as redis_mock:
        redis_mock.get.return_value = None
        contact_id = 1
        response = client.delete(
            f"api/contacts/{contact_id}",
            headers={"Authorization": f"Bearer {token}"}
        )

        assert response.status_code == 200, response.text
        data = response.json()
        assert "id" in data
        assert data["id"] == contact_id
        # Perform additional assertions if needed


def test_get_contacts_birthday(client, token):
    with patch.object(auth_service, "r") as redis_mock:
        redis_mock.get.return_value = None
        response = client.get("/api/contacts/birthday_contacts/", headers={"Authorization": f"Bearer {token}"})

        assert response.status_code == 200, response.text
        data = response.json()
        assert isinstance(data, list)
