ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION}

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "hw_django/manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
