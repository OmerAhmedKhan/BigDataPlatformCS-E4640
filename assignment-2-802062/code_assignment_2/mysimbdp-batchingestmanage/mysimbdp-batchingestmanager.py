import logging
import os
import sys
import json
import pandas as pd

user_home_dir = os.path.expanduser('~')
root_path_to_client_stream_script_dir = '{}/code_assignment_2/mysimbdp-streamingestmanager/'.format(user_home_dir)
logging.basicConfig(filename='batchingestmanager.log',
                            filemode='a',
                            format='%(asctime)s, %(process)d %(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

def write_csv_to_db(client, path, tenant):
    db = client.mydb
    df = pd.read_csv(path)

    records = json.loads(df.T.to_json()).values()
    try:
        # batching
        db.things.insert_many(records)
    except Exception as e:
        logging.error("Unable to process request due to {}".format(str(e)))
        logging.info("Going for a steaming solution")
        client_stream_dir_path = '{}{}/'.format(root_path_to_client_stream_script_dir, tenant)
        sys.path.insert(1, client_stream_dir_path)
        from clientstreamingestapp import start, stop
        start(client, tenant)

    return True
