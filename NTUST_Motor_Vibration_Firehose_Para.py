from pymongo import MongoClient
import requests
import time
import argparse
import datetime
import random
import logging
from logging.config import fileConfig

def firehose(time_counter, machine_id_list, collection, feature_extraction_post_url, classifier_post_url):
    logger = logging.getLogger(__name__)

    data_list = []
    for machine_id in machine_id_list:
        cnt = collection.count({"Time": str(time_counter), "Machine_ID": machine_id})
        if cnt == 0:
            logger.warn('%s query no result' % (machine_id))
            continue
        elif cnt > 1:
            logger.warn(machine_id + ' multi results')
            continue
            
        for a in collection.find({"Time": str(time_counter), "Machine_ID": machine_id}):
            del a['_id']
            data_list.append(a)
            logger.info('Machine_ID:%s, Time:%s, key name V1 length: %s' % (machine_id, time_counter, len(a['V1'])))

    for data in data_list:
        r = requests.post(feature_extraction_post_url, json=data)
        logger.info((data['Machine_ID'], r.status_code, r.reason, 'feature_extraction', r.elapsed.total_seconds()))

        # debug
        # with open('log.txt','w') as f:
        #     f.write(r.text)
        # print(r.text)

        # post to classifier url
        r = requests.post(classifier_post_url, json=data)
        logger.info((data['Machine_ID'], r.status_code, r.reason, 'classifier', r.elapsed.total_seconds()))

def main():
    fileConfig('logging.ini')
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-m', '--machine', default="A",
                        help='Machine ID list split by comma')
    parser.add_argument('-d', '--database', default="8de65d74-0a4a-470f-8aff-c7726498edbb",
                        help='MongoDB database name')
    parser.add_argument('-u', '--user', default="f63a3768-ad05-45c2-a5ad-9de0213d3337",
                        help='MongoDB user name')
    parser.add_argument('-p', '--password', default="pnXRCpWxdP0lUIvYZV3jaA0bI",
                        help='MongoDB password')
    parser.add_argument('-H', '--host', default="124.9.14.76",
                        help='MongoDB host')
    parser.add_argument('-c', '--collection', default="ntust",
                        help='MongoDB collection name')
    parser.add_argument('-e', '--postfe', default="https://532735e7-98aa-4aea-a93b-8ad3d84f4eec-NTUST-Motor-FFT-dev.iii-cflab.com",
                        help='Post feature extraction post url')
    parser.add_argument('-y', '--postclassify', default="http://cf-json-matching.iii-cflab.com/firehose_post",
                        help='Post classifier post url')
    parser.add_argument('-b', '--begin', default=0,
                        help='Begin timestamp')
    parser.add_argument('-n', '--end', default=3,
                        help='End timestamp')
    parser.add_argument('-i', '--interval', default=2,
                        help='Send time interval (second)')

    args = parser.parse_args()
    machine_id_list = args.machine.split(',')
    database = args.database
    user = args.user
    password = args.password
    host = args.host
    collection = args.collection
    feature_extraction_post_url = args.postfe
    classifier_post_url = args.postclassify
    begin_timestamp = int(args.begin)
    end_timestamp = int(args.end)
    interval = args.interval
    logger.info(args)

    mongo_uri = "mongodb://%s:%s@%s:27017/%s" % (user, password, host, database)
    client = MongoClient(mongo_uri)
    db = client[database]
    clct = db[collection]

    send_counter = 0
    while True:
        time_counter = random.randint(begin_timestamp, end_timestamp-1)
        firehose(time_counter, machine_id_list, clct, feature_extraction_post_url, classifier_post_url)
        time.sleep(float(interval))
        send_counter = send_counter + 1
        logger.info('Send counter: %s' % (send_counter))

if __name__ == '__main__':
    main()