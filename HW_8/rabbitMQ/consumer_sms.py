import time
import json

import pika

from rabbitMQ.produser import Client

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_SMS', durable=True)
print(' [*] Waiting for SMS. To exit press CTRL+C')


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f" [x] Received SMS {message}")
    time.sleep(1)
    clients = Client.objects()
    for client in clients:
        client.update(status=True)
    print(f" [x] Sent SMS: {method.delivery_tag} ")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_SMS', on_message_callback=callback)

if __name__ == '__main__':
    channel.start_consuming()
