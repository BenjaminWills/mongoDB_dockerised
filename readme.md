# Dockerising mongo db

Small project to:

- dockerise a mongo db instance
- persist the data beyond shutting down the docker container
- python api queries to the database.

## How to run

To enter the docker container via the shell:

```sh
docker exec -it mongodb4.0 bash
```

Then enter into the mongoDB instance with the command:

```sh
mongo -u root -p
```

Where:

- `-u` stands for `username`
- `-p` stands for `password`

You will be prompted for a `password` after writing this prompt

## Connecting with python

The `API` is called `pymongo`, we connect via the connection string:

```python
import pymongo

CONNECTION_STRING = "mongodb://<username>:<password>@host:port/defaultauthdb?options"

client = pymongo.MongoClient(CONNECTION_STRING)
```

for more info on this check out my programming notes repo @ [programming notes](https://github.com/BenjaminWills/programming-notes/blob/master/MongoDB/Mongo%20DB.md)
