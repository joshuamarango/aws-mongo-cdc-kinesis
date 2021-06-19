import os
import auth
from pymongo import (
    MongoClient
)

class MongoChangeStream:
    def __init__(self) -> None:
        self.mongo_client:MongoClient = auth.MongoAuthentication().connect()
        self.watch_option:str = os.environ.get("WATCH_OPTION")
    
    def __watch_all(self):
        """Watch entire mongo instance and all its databases"""
        print("watching all databases and collections")
        
    def __watch_database(self):
        """Watch entire database and all its collections"""
        print("watching all collections within [x] database")
        
    def __watch_collection(self):
        """Watch entire collection"""
        print("watching [x] collection")
        
    def start(self) -> None:
        """
        Start MongoDB change stream with watch type selected.
        Default watch option will be all if none is configured.
        """
        mongo_watch_options = {
            "ALL": self.__watch_all(),
            "DATABASE": self.__watch_database(),
            "COLLECTION": self.__watch_collection()
        }
        
        return mongo_watch_options(self.watch_option, self.__watch_all())