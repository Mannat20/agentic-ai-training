from pymongo import MongoClient
from pymongo.server_api import ServerApi

class DBHelper:
    def __init__(self,db_name='Agentic_AI'):
        uri = "mongodb+srv://mannat20_db_user:<password>@cluster0.8tjcfyy.mongodb.net/?appName=Cluster0"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db=self.client[db_name]
        print('[DBHelper] Connection Created')

    def select_collection(self,collection='users'):
        self.collection=self.db[collection]
        print('[DBHelper] Collection Selected:"', collection)
    
    def save_document(self,document):
        inserted_id=self.collection.insert_one(document)
        print('[DBHelper] Document Saved. Id is:', inserted_id)