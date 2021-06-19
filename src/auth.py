import os
from pymongo import (
    MongoClient,
    errors as MongoErrors
)

class MongoAuthentication:
    def __init__(self, mongodb_uri:str) -> None:
        """Class initialised by fetching MongoDB URI from env"""
        self.mongo_client:str = mongodb_uri
        
    def connect(self) -> MongoClient:
        """Connect to MongoDB instance using provided URI"""
        try:
            mongo_client = MongoClient(self.mongo_client)
            mongo_client.admin.command("ismaster")
            return mongo_client
        except MongoErrors.ConnectionFailure:
            print("Server not available")
    