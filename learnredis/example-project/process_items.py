#!/usr/bin/env python
import json
import redis
import pymongo

def main():
    r = redis.Redis(host='127.0.0.1',port=6379,db=0)
    client = pymongo.MongoClient(host='127.0.0.1', port=12345)
    db = client['dmoz']
    collection = db['sheet']
    while True:
        # process queue as FIFO, change `blpop` to `brpop` to process as LIFO
        source, data = r.blpop(["myspider_redis1:items"])
        item = json.loads(data)
        collection.insert(item)
	print('process')
if __name__ == '__main__':
    main()
