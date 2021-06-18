import auth

def main(uri:str):
    mongo_client = auth.Auth.connect()

if __name__ == "__main__":
    main("mongodb://localhost:27017/admin")