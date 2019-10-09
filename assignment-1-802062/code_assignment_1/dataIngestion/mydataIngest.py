import argparse
from helper import read_db, write_csv_to_db

from pymongo import MongoClient

client = MongoClient('34.69.192.142', 27017, username='root', password='FoSezeYin7Qr', authSource='admin')

parser = argparse.ArgumentParser(description='Data Ingest from CSV to CoreDms')
parser.add_argument('-p','--path', help='Path to csv file')
parser.add_argument('-o','--operation', help='To read records enter r else w', required=True)

args = vars(parser.parse_args())



if args['operation'] == 'r':
    print(read_db(client))

elif args['path'] and args['operation'] == 'w':
    path = args['path']
    write_csv_to_db(client, path)

else:
    print('Please select correct arrguments')


