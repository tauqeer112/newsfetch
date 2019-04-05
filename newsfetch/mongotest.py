from pymongo import MongoClient

cars = [{'name': 'Audi', 'price': 52642},
        {'name': 'Mercedes', 'price': 57127},
        {'name': 'Skoda', 'price': 9000},
        {'name': 'Volvo', 'price': 29000},
        {'name': 'Bentley', 'price': 350000},
        {'name': 'Citroen', 'price': 21000},
        {'name': 'Hummer', 'price': 41400},
        {'name': 'Volkswagen', 'price': 21600}]

client = MongoClient('mongodb://fouthpillar:pillar@cluster0-shard-00-00-lv2tm.mongodb.net:27017,cluster0-shard-00-01-lv2tm.mongodb.net:27017,cluster0-shard-00-02-lv2tm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')

with client:

    db = client.testdb

    db.cars.insert_many(cars)
