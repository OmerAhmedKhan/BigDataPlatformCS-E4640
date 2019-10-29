import sys
import json
import glob
from pymongo import MongoClient
import logging

logging.basicConfig(filename='error.log',level=logging.ERROR)
client = MongoClient('34.69.192.142', 27017, username='root', password='FoSezeYin7Qr', authSource='admin')
root_path_to_client_dir = '/home/oak/mysimbdp-client-dir/'

def get_config(file_name, tenant):
    try:
        with open(file_name, 'r') as f:
            config = json.load(f)
        if not config.get(tenant):
            logging.error("Tenant not found")
            return

        return config.get(tenant)

    except Exception:
        logging.error("Unable to read config file")
        return


def execute_batch_script(file_name, tenant):
    client_dir_path = '{}{}'.format(root_path_to_client_dir,tenant)
    sys.path.insert(1, client_dir_path)
    from clientbatchingestapp import write_csv_to_db
    for file in glob.glob('{}/{}.csv'.format(client_dir_path, file_name)):
        write_csv_to_db(client, file)

def execute_stream_script(tenant, operation='stop'):
    client_dir_path = '{}{}'.format(root_path_to_client_dir,tenant)
    sys.path.insert(1, client_dir_path)
    from clientbatchingestapp import start, stop
    if operation == 'start':
        start(client, tenant)
    else:
        stop()

    return 


def get_data_files(tenant):
    files = []
    client_dir_path = '{}{}'.format(root_path_to_client_dir, tenant)
    for file in glob.glob('{}/*.csv'.format(client_dir_path)):
        files.append(file.split('/')[-1])


