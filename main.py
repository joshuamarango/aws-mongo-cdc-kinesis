import pymongo
from pymongo.errors import ConnectionFailure as MongoConnectionFailure

def main(uri:str):
    mongo_client = pymongo.MongoClient(uri)
    try:
        mongo_client.admin.command("ismaster")
    except MongoConnectionFailure:
        print("Server not available")

if __name__ == "__main__":
    main("mongodb://localhost:27017/admin")