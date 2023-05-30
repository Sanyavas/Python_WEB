from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch
from src.database.models import User

client = TestClient(app)


def get_fake_user(confirmed=True):
    user_data = {
        "id": 1,
        "username": "test_user",
        "email": "test@example.com",
        "password": "password",
        "confirmed": confirmed,
    }
    return User(**user_data)


@patch('src.services.auth.auth_service.decode_refresh_token', return_value="example@example.com")
@patch('src.repository.users.get_user_by_email', return_value=get_fake_user())
def test_refresh_token_invalid_refresh_token(mock_get_user_by_email, mock_decode_refresh_token):
    response = client.get("/api/auth/refresh_token", headers={"Authorization": "Bearer invalid_token"})
    assert response.status_code == 401


@patch('src.services.auth.auth_service.get_email_from_token', return_value="example@example.com")
@patch('src.repository.users.get_user_by_email', return_value=None)
def test_confirmed_email_verification_error(mock_get_user_by_email, mock_get_email_from_token):
    response = client.get("/api/auth/confirmed_email/invalid_token")
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Verification error"


@patch('src.services.auth.auth_service.get_email_from_token', return_value="example@example.com")
@patch('src.repository.users.get_user_by_email', return_value=get_fake_user(confirmed=True))
def test_confirmed_email_already_confirmed(mock_get_user_by_email, mock_get_email_from_token):
    response = client.get("/api/auth/confirmed_email/valid_token")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Your email is already confirmed"


@patch('src.services.auth.auth_service.get_email_from_token', return_value="example@example.com")
@patch('src.repository.users.get_user_by_email', return_value=get_fake_user(confirmed=False))
@patch('src.repository.users.confirmed_email')
def test_confirmed_email_success(mock_confirmed_email, mock_get_user_by_email, mock_get_email_from_token):
    response = client.get("/api/auth/confirmed_email/valid_token")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Email confirmed"


@patch('src.repository.users.get_user_by_email', return_value=get_fake_user(confirmed=False))
@patch('src.routes.auth.send_email')
def test_request_email(mock_send_email, mock_get_user_by_email):
    response = client.post("/api/auth/request_email", json={"email": "example@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Check your email for confirmation."
