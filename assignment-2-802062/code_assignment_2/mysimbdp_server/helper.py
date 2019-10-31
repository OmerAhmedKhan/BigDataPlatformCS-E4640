import sys
import json
import glob
from pymongo import MongoClient
import logging
import requests
from requests.auth import HTTPBasicAuth
import os

user_home_dir = os.path.expanduser('~')
logging.basicConfig(filename='error.log',level=logging.ERROR)
client = MongoClient('<insert_ip>', 27017, username='<insert_user>', password='<insert_password>', authSource='admin')
root_path_to_client_data_dir = '{}/mysimbdp-client-dir/'.format(user_home_dir)
root_path_to_client_batch_script_dir = '{}/code_assignment_2/mysimbdp-batchingestmanager'.format(user_home_dir)
root_path_to_client_stream_script_dir = '{}/code_assignment_2/mysimbdp-streamingestmanager/'.format(user_home_dir)


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
    client_batch_dir_path = '{}{}'.format(root_path_to_client_batch_script_dir,tenant)
    client_data_dir_path = '{}{}'.format(root_path_to_client_data_dir,tenant)
    sys.path.insert(1, client_batch_dir_path)
    from clientbatchingestapp import write_csv_to_db
    for file in glob.glob('{}/{}.csv'.format(client_data_dir_path, file_name)):
        write_csv_to_db(client, file)

def execute_stream_script(tenant, operation='stop'):
    client_stream_dir_path = '{}{}/'.format(root_path_to_client_stream_script_dir, tenant)
    sys.path.insert(1, client_stream_dir_path)
    from clientstreamingestapp import start, stop
    if operation == 'start':
        start(client, tenant)
    else:
        stop()

    return True


def get_data_files(tenant):
    files = []
    client_data_dir_path = '{}{}/'.format(root_path_to_client_data_dir, tenant)
    for file in glob.glob('{}/*.csv'.format(client_data_dir_path)):
        files.append(file.split('/')[-1])

    return files


def monitor_stream_ingestion(tenant):
    response = requests.get('http://localhost:15672/api/queues/%2F/{}_queue'.format(tenant), auth=HTTPBasicAuth('guest', 'guest'))
    return json.loads(response.content)