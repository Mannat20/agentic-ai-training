from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mannat20_db_user:<password>@cluster0.8tjcfyy.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db=client['Agentic_AI']
names=db.list_collection_names
print(names)