#!/usr/bin/env python
import pika
import json
import logging

logging.basicConfig(filename='tenant.log',level=logging.ERROR)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_ingestion', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

def ingest_data(client, tenant, data):
    db = client[tenant]
    try:
        db.things.insert(data)
    except Exception as e:
        logging.error(e)
        return False

    return True

def start(client, tenant):

    channel.queue_bind(
        exchange='direct_ingestion', queue=queue_name, routing_key=tenant)


    def callback(ch, method, properties, body):
        if method.routing_key == tenant:
            data = json.loads(body)
            ingest_data(client, tenant, data)
            logging.info('data added')


    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

def stop():
    connection.close()