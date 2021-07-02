from pymongo import MongoClient
from aws_mongo_cdc_kinesis.core.auth import MongoAuthentication
import mockupdb


def test_mongodb_auth_connection():
    """Test the auth service to make sure we can authenticate into Mongo"""
    server: mockupdb.MockupDB = mockupdb.MockupDB(auto_ismaster={"maxWireVersion": 3})
    server.run()
    mongo_client: MongoClient = MongoAuthentication(server.uri).connect()
    return mongo_client.server_info()


print(test_mongodb_auth_connection())
