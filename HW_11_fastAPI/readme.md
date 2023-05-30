# Змінні оточення


* '.env
* POSTGRES_USER="name_user"
* POSTGRES_PASSWORD="password"
* POSTGRES_DB_NAME="name_postgres"
* POSTGRES_DOMAIN="domain"
* POSTGRES_PORT="port

* SQLALCHEMY_DATABASE_URL=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_DOMAIN}:${POSTGRES_PORT}/${POSTGRES_DB_NAME}

* JWT_SECRET_KEY="secret_key"
* JWT_ALGORITHM="HS256"

* REDIS_HOST="localhost"
* REDIS_PORT="6379"

* MAIL_USERNAME="example@meta.ua"
* MAIL_PASSWORD="password"
* MAIL_FROM=${MAIL_USERNAME}
* MAIL_PORT="465"
* MAIL_SERVER="smtp.meta.ua"

* CLOUDINARY_NAME='cloudinary_name'
* CLOUDINARY_API_KEY='0000000000000000'
* CLOUDINARY_API_SECRET='secret'


Запуск тестів

```bash
pytest --cov=. --cov-report html tests/
```