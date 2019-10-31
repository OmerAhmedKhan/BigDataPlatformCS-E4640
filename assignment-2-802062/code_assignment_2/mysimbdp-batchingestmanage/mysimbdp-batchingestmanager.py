import argparse
import glob
import sys
import os

from pymongo import MongoClient

client = MongoClient('34.69.192.142', 27017, username='root', password='FoSezeYin7Qr', authSource='admin')
user_home_dir = os.path.expanduser('~')
root_path_to_client_dir = '{}/mysimbdp-client-dir/'.format(user_home_dir)

parser = argparse.ArgumentParser(description='Data Ingest from client source file to CoreDms')
parser.add_argument('-p','--path', help='Path to source file', required=True)
parser.add_argument('-t','--tenant_id', help='Tenant id', required=True)

args = vars(parser.parse_args())
if args['path'] and args['tenant_id']:

    client_dir_path = '{}{}'.format(root_path_to_client_dir, args['tenant_id'])
    sys.path.insert(1, args['path'])
    from clientbatchingestapp import write_csv_to_db
    for file in glob.glob('{}{}/*.csv'.format(root_path_to_client_dir, args.get('tenant_id', ''))):
        write_csv_to_db(client, file)
else:
    print('Please select correct arrguments')
