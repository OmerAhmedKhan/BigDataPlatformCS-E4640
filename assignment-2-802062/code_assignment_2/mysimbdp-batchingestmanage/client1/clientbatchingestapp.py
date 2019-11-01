import pandas as pd
import json
import logging

logging.basicConfig(filename='client.log',
                            filemode='a',
                            format='%(asctime)s, %(process)d %(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)


def write_csv_to_db(client, path):
    db = client.mydb
    df = pd.read_csv(path)

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