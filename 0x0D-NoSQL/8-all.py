#!/usr/bin/env python3
""" Mongo documents module.
"""


def list_all(mongo_collection):
    """ Method that lists all documents in a collection.
        Arg:
            mongo_collection: pymongo collection object.
        Return:
            An empty list if no document in the collection.
    """
    return mongo_collection.find()
