# Import libs
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import logging

logging.basicConfig(filename='cusomterApp.log',level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def process_stream_analytics(client, tenant, window_size):
    sc = SparkContext(appName="StreamingAlarmCount")
    # 2 is the batch interval : 4 seconds
    ssc = StreamingContext(sc, 5)

    lines = ssc.socketTextStream('localhost', 9999)

    counts = lines.flatMap(lambda line: [line.get('value'), line.get('valueThreshold')]) \
        .filter(lambda word: word[4] > word[5]) \
        .map(lambda word: (word, 1)) \
        .reduceByKeyAndWindow(lambda a, b: a + b, window_size, 2) # Window of 10 sec interval

    try:
        db = client[tenant]
        db.things.insert_many(counts)
    except Exception as e:
        logging.error("Unable to process request due to {}".format(str(e)))
        return False

    ssc.start()
    ssc.awaitTermination()

