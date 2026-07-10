
from pymongo import MongoClient # here Captil letter of M and C shows that MongoClient is a class .
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mannat20_db_user:<password>@cluster0.8tjcfyy.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)