#!/usr/bin/env python
import pika
import sys
import argparse
import pandas as pd
import json


parser = argparse.ArgumentParser(description='Data Ingest from CSV to CoreDms through stream')
parser.add_argument('-t','--tenant', help='Tenant ID', required=True)
parser.add_argument('-f','--file_path', help='Path of CSV file to export to CoreDMS', required=True)

args = vars(parser.parse_args())

if not all([args['tenant'], args['file_path']]):
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
for records in records:
    channel.basic_publish(
        exchange='direct_logs', routing_key=tenant, body=json.dumps(record))

connection.close()