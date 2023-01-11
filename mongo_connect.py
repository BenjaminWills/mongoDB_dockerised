import pymongo

CONNECTION_STRING = "mongodb://root:password@localhost:27017"

with pymongo.MongoClient(CONNECTION_STRING) as client:
    data = client["data"]
    users = data["users"].find()
    for user in users:
        print(user)
    client.close()
