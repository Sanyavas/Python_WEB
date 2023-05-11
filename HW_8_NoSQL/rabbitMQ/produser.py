from datetime import datetime
from random import choice
from faker import Faker
import json

import pika

from mongoengine import Document, StringField, connect, BooleanField, EmailField

from normalize_phone import normalize_phone

fake = Faker('uk-UA')
connect(host="mongodb://localhost:27017/hw8")


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_Email', durable=True)
channel.queue_declare(queue='task_SMS', durable=True)


class Client(Document):
    name = StringField(required=True)
    email = EmailField()
    phone = StringField(max_length=15)
    status = BooleanField()
    type_message = StringField(max_length=50)


def load_client():
    for _ in range(25):
        Client(
            name=fake.name(),
            email=fake.email(),
            phone=normalize_phone(fake.phone_number()),
            status=False,
            type_message=choice(["SMS", "Email"])
        ).save()


def main():
    clients = Client.objects()
    for client in clients:
        message = {
            "id": str(client.id),
            "message": f"Congratulations! Putin is dead!!!",
            "date": datetime.now().isoformat()
        }
        if client.type_message == "SMS":
            channel.basic_publish(exchange='', routing_key='task_SMS', body=json.dumps(message).encode())
        elif client.type_message == "Email":
            channel.basic_publish(exchange='', routing_key='task_Email', body=json.dumps(message).encode())
        print(" [x] Sent %r" % message)
    connection.close()


if __name__ == '__main__':
    # load_client()
    main()
