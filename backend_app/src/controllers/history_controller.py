import logging
from typing import Dict, List

from backend_app.src.schemas.iris_response import IrisResponse
from backend_app.src.services.history_service import HistoryService

class HistoryController:

    '''
    Class containing controllers methods for the history endpoints.
    '''

    def __init__(self) -> None:
        self.__history_service = HistoryService()

    def get_history(self) -> Dict[str, List[IrisResponse]]:
        '''
        Method to return all of the previous predictions in the database

        Parameters:
            No parameters

        Returns:
            Dictionary with all of the predictions
        '''
        try:
            history_collection = self.__history_service.get_history()

            response = [IrisResponse.model_validate(history) for history in history_collection]

            return {
                'history': response
            }

        except Exception as e:
            logging.error(f'Unexpected error: {e}')