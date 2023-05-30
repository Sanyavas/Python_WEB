from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str = "postgresql+psycopg2://postgres:password@domain:5433/database"
    jwt_secret_key: str = "secret_key"
    jwt_algorithm: str = "HS256"
    mail_username: str = "example@meta.ua"
    mail_password: str = "password"
    mail_from: str = "example@meta.ua"
    mail_port: int = 465
    mail_server: str = "smtp.test.com"
    redis_host: str = 'localhost'
    redis_port: int = 6379
    redis_password: str = 'password'
    cloudinary_name = 'cloudinary_name'
    cloudinary_api_key = '0000000000000000'
    cloudinary_api_secret = 'secret'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
