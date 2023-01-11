import pymongo

CONNECTION_STRING = "mongodb://root:password@localhost:27017"

with pymongo.MongoClient(CONNECTION_STRING) as client:
    users = client["data"]
    items = users["users"].find()
    for item in items:
        print(item)
    client.close()
