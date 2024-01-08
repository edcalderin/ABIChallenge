from typing import Dict, List
from datetime import datetime

from backend_app.src.services.connection import MongoDatabase

class PredictionService:

    def __init__(self) -> None:
        self.__database = MongoDatabase.get_database()
        self.__collection_predictions = self.__database['collection_predictions']

    def insert_one_prediction(self, prediction: Dict):
        self.__collection_predictions.insert_one(prediction)

    def insert_batch_predictions(self, predictions: List[Dict]):
        self.__collection_predictions.insert_many(predictions)

    def get_prediction(self, date: datetime = None):
        if date is None:
            return self.__collection_predictions
        else:
            return self.__collection_predictions.find({'date': date})