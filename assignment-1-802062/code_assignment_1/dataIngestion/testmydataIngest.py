import time
from pymongo import MongoClient
from helper import write_csv_to_db, read_db
import logging

logging.basicConfig(filename='dataIngestPerformanceRead.log',
                            filemode='a',
                            format='%(asctime)s, %(process)d %(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)



client = MongoClient('34.69.192.142', 27017, username='root', password='FoSezeYin7Qr', authSource='admin')
path = "../../data/googleplaystore.csv"

tic = time.clock()
read_db(client)
toc = time.clock()
logging.info("Time to execute read from dataingestion is: {}".format(toc-tic))
print(toc-tic)