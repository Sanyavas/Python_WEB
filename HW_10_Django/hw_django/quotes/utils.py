from pymongo import MongoClient


def get_mongodb():
    """
    The get_mongodb function connects to the MongoDB database and returns a handle to it.
    """
    client = MongoClient("mongodb://localhost")

    db = client.hw
    return db
