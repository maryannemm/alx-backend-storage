#!/usr/bin/env python3
""" 8-all """

def list_all(mongo_collection):
    """Lists all documents in a collection."""
    return list(mongo_collection.find()) if mongo_collection.count_documents({}) > 0 else []
