import cloudinary
from unittest.mock import MagicMock, patch
from src.services.upload_avatar import UploadService


def test_upload():
    # Замінюємо метод upload об'єкта cloudinary.uploader
    # на моканий об'єкт відповіді
    mock_response = {
        "public_id": "sample_id",
        "version": 123,
        "url": "https://example.com/image.jpg"
    }
    cloudinary.uploader.upload = MagicMock(return_value=mock_response)

    # Викликаємо метод upload з класу UploadService
    file = "sample_file"
    public_id = "sample_id"
    result = UploadService.upload(file, public_id)

    # Перевіряємо результат
    assert result == mock_response


def test_get_url_avatar():
    # Замінюємо метод build_url об'єкта cloudinary.CloudinaryImage
    # на моканий результат url
    mock_url = "https://example.com/image.jpg"
    cloudinary.CloudinaryImage.build_url = MagicMock(return_value=mock_url)

    # Викликаємо метод get_url_avatar з класу UploadService
    public_id = "sample_id"
    version = 123
    result = UploadService.get_url_avatar(public_id, version)

    # Перевіряємо результат
    assert result == mock_url
