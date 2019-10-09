import time
from pymongo import MongoClient
from dataIngestion.helper import write_csv_to_db

client = MongoClient('34.69.192.142', 27017, username='root', password='FoSezeYin7Qr', authSource='admin')
path = "/home/oak/Downloads/googleplaystore.csv"

tic = time.clock()
write_csv_to_db(client, path)
toc = time.clock()
print(toc-tic)