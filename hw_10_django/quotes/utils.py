from pymongo import MongoClient
from django.conf import settings


def get_mongodb():
    uri = settings.MONGO_URI
    client = MongoClient(uri)
    try:
        db = client.web16_hw10
    except Exception as e:
        print(e)

    return db
