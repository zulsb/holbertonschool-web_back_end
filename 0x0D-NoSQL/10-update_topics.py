#!/usr/bin/env python3
""" Mongo change school topics module.
"""


def update_topics(mongo_collection, name, topics):
    """ Method that changes all topics of a school document based on the name.
        Arg:
            mongo_collection: pymongo collection object.
            name: Is the school name to update.
            topipcs: Is the list of topics approached in the school.
        Return:
            The update topics.
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
