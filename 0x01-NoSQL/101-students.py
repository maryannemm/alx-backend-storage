#!/usr/bin/env python3

'''Task 14's module.
'''
def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Parameters:
    mongo_collection: pymongo collection object

    Returns:
    List of students with their average score, sorted by averageScore.
    """
    pipeline = [
        {"$project": {
            "name": 1,
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]

    return list(mongo_collection.aggregate(pipeline))

