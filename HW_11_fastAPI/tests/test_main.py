from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from sqlalchemy.exc import SQLAlchemyError


from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    print(response)
    assert response.status_code == 200


def test_healthchecker_db():
    mock_get_db = MagicMock()
    with patch('src.database.db.get_db', mock_get_db):
        response = client.get("/api/healthchecker/")

        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to FastAPI!"}


# def test_healthchecker_db_error():
#     with patch('src.database.db.get_db') as mock_get_db:
#         mock_db = MagicMock()
#         mock_db.execute.side_effect = SQLAlchemyError()
#         mock_get_db.return_value = mock_db
#
#         response = client.get("/api/healthchecker/")
#
#         assert response.status_code == 500
#         assert response.json() == {"detail": "Error connecting to the database"}
#
#
# def test_healthchecker_db_not_configured():
#     with patch('src.database.db.get_db') as mock_get_db:
#         mock_db = MagicMock()
#         mock_db.execute.return_value = None
#         mock_get_db.return_value = mock_db
#
#         response = client.get("/api/healthchecker/")
#
#         assert response.status_code == 500
#         assert response.json() == {"detail": "Database is not configured correctly"}
