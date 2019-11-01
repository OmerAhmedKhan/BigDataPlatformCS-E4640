#!/usr/bin/env python
import pika
import json
import logging
from multiprocessing import Pool

def close_async_connection(connection):
    connection.close()
    return

logging.basicConfig(filename='tenant.log',level=logging.ERROR)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_ingestion', exchange_type='direct')

# result = channel.queue_declare(queue='{}_queue'.format(tenant), exclusive=True)
# queue_name = result.method.queue

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

    queue_name = set_queue(tenant)
    channel.queue_bind(
        exchange='direct_ingestion', queue=queue_name, routing_key=tenant)

    print("Wait for messages from Producer...")


    def callback(ch, method, properties, body):
        if method.routing_key == tenant:
            data = json.loads(body)
            ingest_data(client, tenant, data)
            logging.info('data added')
            print('data added')


    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    pool = Pool(processes=1)  # Start a worker processes.
    pool.apply_async(close_async_connection, [10], channel.start_consuming)
    #channel.start_consuming()

    return True

def stop():
    connection.close()
    return