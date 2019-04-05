# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
import pymongo


class NewsfetchPipeline(object):
    def open_spider(self, spider):
        hostname = 'piro.ceubekalawiz.us-east-2.rds.amazonaws.com'  # host
        username = 'piro'  # username
        password = 'research123'  # your password
        database = 'piro'  # database name
        self.client = pymongo.MongoClient(
            "mongodb://fouthpillar:pillar@cluster0-shard-00-00-lv2tm.mongodb.net:27017,cluster0-shard-00-01-lv2tm.mongodb.net:27017,cluster0-shard-00-02-lv2tm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
        self.client.close()

    def process_item(self, item, spider):
        if spider.name == 'republic':
            # self.cur.execute(
            #     "insert into feed_republic(headline,link) values(%s,%s)", (item['headline'], item['link']))
            # self.connection.commit()
            with self.client:
                db = self.client['newsdb']
                collection = db['feed_republic']
                data = {"headline": item['headline'], "link": item['link']}
                x = collection.insert_one(data)
                print(x.inserted_id)

            return item

        if spider.name == 'ndtv':
            # self.cur.execute(
            #     "insert into feed_ndtv(headline,link) values(%s,%s)", (item['headline'], item['link']))
            # self.connection.commit()
            with self.client:
                db = self.client['newsdb']
                collection = db['feed_ndtv']
                data = {"headline": item['headline'], "link": item['link']}
                x = collection.insert_one(data)
                print(x.inserted_id)

            return item

        if spider.name == 'indiatv':
            # self.cur.execute(
            #     "insert into feed_indiatv(headline,link) values(%s,%s)", (item['headline'], item['link']))
            # self.connection.commit()
            with self.client:
                db = self.client['newsdb']
                collection = db['feed_indiatv']
                data = {"headline": item['headline'], "link": item['link']}
                x = collection.insert_one(data)
                print(x.inserted_id)

            return item

        if spider.name == 'thehindu':
            # self.cur.execute(
            #     "insert into feed_thehindu(headline,link) values(%s,%s)", (item['headline'], item['link']))
            # self.connection.commit()
            with self.client:
                db = self.client['newsdb']
                collection = db['feed_thehindu']
                data = {"headline": item['headline'], "link": item['link']}
                x = collection.insert_one(data)
                print(x.inserted_id)

            return item

        if spider.name == 'zee':
            # self.cur.execute(
            #     "insert into feed_zeenews(headline,link) values(%s,%s)", (item['headline'], item['link']))
            # self.connection.commit()
            with self.client:
                db = self.client['newsdb']
                collection = db['feed_zeenews']
                data = {"headline": item['headline'], "link": item['link']}
                x = collection.insert_one(data)
                print(x.inserted_id)

            return item
