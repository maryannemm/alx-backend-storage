#!/usr/bin/env python3

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Parameters:
    mongo_collection: pymongo collection object
    topic (string): topic to search for

    Returns:
    List of schools with the specific topic.
    """
    return mongo_collection.find({"topics": topic})

