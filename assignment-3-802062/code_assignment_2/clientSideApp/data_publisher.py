#!/usr/bin/env python
import pika
import sys
import argparse
import pandas as pd
import json
import logging

logging.basicConfig(filename='publisher.log',level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

parser = argparse.ArgumentParser(description='Data Ingest from CSV to CoreDms through stream')
parser.add_argument('-t','--tenant', help='Tenant ID', required=True)
parser.add_argument('-f','--file_path', help='Path of CSV file to export to CoreDMS', required=True)

args = vars(parser.parse_args())

if not all([args['tenant'], args['file_path']]):
    logging.error('Please select correct arrguments ')
    print('Please select correct arrguments')
    sys.exit()

tenant = args['tenant']
file_path = args['file_path']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_ingestion', exchange_type='direct')

df = pd.read_csv(file_path)
records = json.loads(df.T.to_json()).values()
for record in records:
    logging.error("Message published: {}".format(json.dumps(record)))
    channel.basic_publish(
        exchange='direct_ingestion', routing_key=tenant, body=json.dumps(record))

connection.close()