from pymongo.cursor import Cursor

from backend_app.src.services.connection import MongoDatabase

class HistoryService:

    def __init__(self) -> None:
        self.__database = MongoDatabase.get_database()
        self.__collection_predictions = self.__database['collection_predictions']

    def get_history(self) -> Cursor:
        return self.__collection_predictions.find()