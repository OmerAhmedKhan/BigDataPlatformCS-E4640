import pandas as pd
import json
import logging

logging.basicConfig(filename='dataIngestPerformance.log',
                            filemode='a',
                            format='%(asctime)s, %(process)d %(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

fields = ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
       'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
       'Android Ver']


def read_db(client, is_id=True, count=0):
    db = client.mydb
    cursor = db.apps.find({}, {'_id': is_id}).limit(count)
    return list(cursor)


def write_csv_to_db(client, path):
    db = client.mydb
    df = pd.read_csv(path)
    print(df.columns)
    for column in df.columns:
        if column not in fields:
            logging.error('Schema error')

    records = json.loads(df.T.to_json()).values()
    try:
        db.things.insert_many(records)
    except Exception as e:
        logging.error("Unable to process request due to {}".format(str(e)))
        return False

    return True

def write_to_db(client, data):
    db = client.mydb

    try:
        db.things.insert(data)
    except Exception as e:
        logging.error("Unable to process request due to {}".format(str(e)))
        return False

    return True
