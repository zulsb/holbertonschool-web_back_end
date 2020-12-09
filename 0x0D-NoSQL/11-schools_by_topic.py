#!/usr/bin/env python3
""" Mongo topic searched module.
"""


def schools_by_topic(mongo_collection, topic):
    """ Method that returns the list of school having a specific topic.
        Arg:
            mongo_collection: pymongo collection object.
            topic: Topic searched.
        Return:
            A list.
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
