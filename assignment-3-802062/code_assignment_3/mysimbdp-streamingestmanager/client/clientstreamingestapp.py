#!/usr/bin/env python
import pika
import logging
import socket

def close_async_connection(connection):
    connection.close()
    return

logging.basicConfig(filename='tenant.log',level=logging.ERROR)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_ingestion', exchange_type='direct')


def ingest_data(client, tenant, data):
    db = client[tenant]
    try:
        db.things.insert(data)
    except Exception as e:
        logging.error(e)
        return False

    return True

def set_queue(tenant):
    result = channel.queue_declare(queue='{}_queue'.format(tenant), passive=True)
    return result.method.queue


def start(client, tenant):
    host = 'localhost'
    port = 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    queue_name = set_queue(tenant)
    channel.queue_bind(
        exchange='direct_ingestion', queue=queue_name, routing_key=tenant)

    print("Wait for messages from Producer...")


    def callback(ch, method, properties, body):
        if method.routing_key == tenant:
            s.send(body)
            logging.info('data streamd')
            print('data streamed')


    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

    return True

def stop():
    connection.close()
    return