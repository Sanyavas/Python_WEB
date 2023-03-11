# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.10.5-slim-buster

# Встановимо робочу директорію усередині контейнера
WORKDIR .

# Скопіюємо інші файли до робочої директорії контейнера
COPY . .

# Встановимо залежності усередині контейнера
RUN pip install -r requirements.txt  # pip freeze > requirements.txt

# Позначимо порт де працює програма всередині контейнера
EXPOSE 3000

# Запустимо нашу програму всередині контейнера
ENTRYPOINT ["python", "server.py"]

VOLUME ./data:/data