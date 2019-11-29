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
        average_rate += x['count']/window_size

    logging.info("Average Alarm count of tenant {} is {}".format(tenant, average_rate))
    return average_rate