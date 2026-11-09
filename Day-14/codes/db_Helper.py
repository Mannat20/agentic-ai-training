from pymongo import MongoClient
from pymongo.server_api import ServerApi

from config import MongoDB_uri

class DBHelper:
    def __init__(self,db_name='Agentic_AI'):
        uri = MongoDB_uri
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db=self.client[db_name]
        print('[DBHelper] Connection Created')

    def select_collection(self,collection='users'):
        self.collection=self.db[collection]
        print('[DBHelper] Collection Selected:"', collection)
    
    def save_document(self,document):
        inserted_id=self.collection.insert_one(document)
        print('[DBHelper] Document Saved. Id is:', inserted_id)
    def retrieve(self,condition=None):
        result=self.collection.find(condition)
        for document in result:
            print(document)
        return result
        
    def update(self,condition=None,update_data=None):
        result=self.collection.update_one(
            condition,
            {'$set':update_data}
        )
        print('[DBHelper] updated',result)
    
    def delete_document(self,condition):
        id=self.collection.delete_one(condition)
        print('[DBHelper] Delete_count.',id.deleted_count)
        return id.deleted_count