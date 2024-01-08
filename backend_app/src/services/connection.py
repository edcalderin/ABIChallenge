from pymongo import MongoClient

class MongoDatabase:
    
    @staticmethod
    def get_database() -> MongoClient:
    
        CONNECTION_STRING = "mongodb://localhost:27017/admin"
        
        client = MongoClient(CONNECTION_STRING)
        
        return client['predictions_db']