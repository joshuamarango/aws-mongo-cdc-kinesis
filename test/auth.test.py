import pytest
import pymongo
from mockupdb import MockupDB

server = MockupDB(auto_ismaster={"maxWireVersion": 3})
server.run()

client = pymongo.MongoClient(server.uri)
collection = client.db.collection

print(client)