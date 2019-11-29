import pandas as pd
import json
import logging

logging.basicConfig(filename='client.log',
                            filemode='a',
                            format='%(asctime)s, %(process)d %(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)


def get_alarm_average(client, tenant, window_size, is_id=True):
    db = client[tenant]
    cursor = db.alarms.find({}, {'_id': is_id}).limit(count)
    average_rate = 0
    for x in cursor:
        average_rate += cursor['count']/window_size

    return average_rate