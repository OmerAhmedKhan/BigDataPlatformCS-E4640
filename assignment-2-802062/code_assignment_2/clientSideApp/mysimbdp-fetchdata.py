import json
import glob
import sys
import os
from shutil import copy
import requests
import logging
import argparse

logging.basicConfig(filename='fetchdata.log',level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

parser = argparse.ArgumentParser(description='Data Ingest from CSV to CoreDms through batch')
parser.add_argument('-t','--tenant', help='Tenant ID', required=True)

args = vars(parser.parse_args())
tenant = args['tenant']
user_home_dir = print(os.path.expanduser('~'))

if not tenant:
    logging.error('Please select correct arrguments ')
    print('Please select correct arrguments')
    sys.exit()

# Use http to get config
try:
    response = requests.get('http://127.0.0.1:5000/getConfig/{}'.format(tenant))
except Exception:
    logging.error("Unable to get Confugurations")
    sys.exit()

config = json.loads(response.content).get('config', {})

dir_path = config.get('dir_path', '')
file_type = config.get('file_type', 'csv')
targeted_files = glob.glob('{}*.{}'.format(dir_path, file_type))

if not len(targeted_files) or len(targeted_files) > config.get('file_number', 0):
    logging.error("File number exceeds {}".format(config.get('file_number', 0)))
    sys.exit()

for fname in targeted_files:
    statinfo = os.stat(fname)
    if statinfo.st_size/1024 > config.get('file_size', 0):
        logging.error("File number exceeds {}".format(config.get('file_number', 0)))
        sys.exit()

    logging.info("copying file {} to mysimbdp-client-dir".format(tenant))
    copy(fname, '{}/mysimbdp-client-dir/{}/'.format(user_home_dir, tenant))
