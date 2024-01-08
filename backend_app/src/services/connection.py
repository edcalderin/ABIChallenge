from pymongo import MongoClient
import os

class MongoDatabase:

    @staticmethod
    def get_database() -> MongoClient:
        MONGO_HOST: str = os.getenv('MONGO_HOST', '127.0.0.1')
        MONGO_PORT: int = int(os.getenv('MONGO_PORT', '27017'))

        CONNECTION_STRING = f'mongodb://{MONGO_HOST}:{MONGO_PORT}/admin'

        client = MongoClient(CONNECTION_STRING)

        return client['predictions_db']