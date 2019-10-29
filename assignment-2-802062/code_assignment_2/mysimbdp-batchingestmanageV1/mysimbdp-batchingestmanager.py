import argparse
import glob
import sys

from pymongo import MongoClient

client = MongoClient('34.69.192.142', 27017, username='root', password='FoSezeYin7Qr', authSource='admin')
root_path_to_client_dir = '/home/oak/mysimbdp-client-dir/'

parser = argparse.ArgumentParser(description='Data Ingest from client source file to CoreDms')
parser.add_argument('-p','--path', help='Path to source file', required=True)
parser.add_argument('-i','--client_id', help='Client id', required=True)

args = vars(parser.parse_args())



if args['path'] and args['client_id']:

    client_dir_path = '{}{}'.format(root_path_to_client_dir, args['client_id'])
    sys.path.insert(1, args['path'])
    from clientbatchingestapp import write_csv_to_db
    for file in glob.glob('{}{}/*.csv'.format(root_path_to_client_dir, args.get('client_id', ''))):
        write_csv_to_db(client, file)
else:
    print('Please select correct arrguments')


