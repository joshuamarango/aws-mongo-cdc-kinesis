from src.auth import MongoAuthentication
import mockupdb

server = mockupdb.MockupDB(auto_ismaster={"maxWireVersion": 3})

def test_mongodb_auth_connection():
    """Test the auth service to make sure we can authenticate into Mongo"""
    server.run()
    mongo_client = MongoAuthentication(server.uri).connect()
    return mongo_client.server_info()


print(test_mongodb_auth_connection())