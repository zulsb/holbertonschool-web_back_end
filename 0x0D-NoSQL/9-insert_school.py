#!/usr/bin/env python3
""" Mongo insert a document module.
"""


def insert_school(mongo_collection, **kwargs):
    """ Method that inserts a new document in a collection based on kwargs.
        Arg:
            mongo_collection: pymongo collection object.
            kwargs:
        Return:
            The new _id.
    """
    insert_document = mongo_collection.insert_one(kwargs)
    return insert_document.inserted_id
