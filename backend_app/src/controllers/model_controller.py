import csv
from fastapi import UploadFile
from io import StringIO
import logging
import pandas as pd
from typing import Dict, List

from backend_app.src.schemas.iris_input import IrisInput
from backend_app.src.schemas.iris_response import IrisResponse
from backend_app.src.services.prediction_service import PredictionService

class ModelController:

    '''
    Class containing controllers methods for the endpoints.
    '''

    def __init__(self, model) -> None:
        self.__model = model
        self.__prediction_service = PredictionService()

    def predict(self, input: IrisInput) -> Dict[str, int]:
        '''
        Predict a single sample

        Parameters:
            input: Object of type IrisInput

        Returns:
            Dictionary containing the prediction
        '''
        try:
            features_df = pd.DataFrame(input.model_dump(), index = [0])

            prediction = self.__model.predict(features_df)[0]

            iris_response = IrisResponse(**input.model_dump() | {'prediction': prediction})

            self.__prediction_service.insert_one_prediction(iris_response.model_dump())

            return {
                'prediction': iris_response
            }

        except Exception as e:
            logging.error(f'Unexpected error: {e}')

    async def __csv_reader(self, csv_file: UploadFile):
        '''
        Yields a record from the csv file

        Parameters:
            csv_file: Csv file

        Returns:
            Generates a record one at a time.
        '''
        try:
            contents =  await csv_file.read()
            buffer = StringIO(contents.decode())
            for record in csv.DictReader(buffer):
                yield IrisInput(**record)
        except Exception as e:
            logging.error(e)
            raise Exception(e)
        finally:
            # New try-except block to cover two approaches: If there are not exceptions and buffer is closed and in case of an exception
            # by trying to read the csv file which arise an error because buffer variable does not exist.
            try:
                buffer.close()
            except Exception as e:
                logging.error('Error while closing buffer {e}')

    async def predict_on_batch(self, csv_file: UploadFile) -> Dict[str, List]:
        '''
        Predict a batch of samples

        Parameters:
            csv_file: Csv file

        Returns:
            Dictionary containing a list of  predictions.
        '''
        try:
            if not csv_file.content_type == 'text/csv':
                error_message: str = 'Invalid csv file'
                raise TypeError(error_message)

            logging.info('Predicting on batch')

            features_list: List[Dict] = [input.model_dump() async for input in self.__csv_reader(csv_file)]

            features_df = pd.DataFrame.from_records(features_list)

            features_df['prediction'] = self.__model.predict(features_df)

            self.__prediction_service.insert_batch_predictions(features_df.to_dict('records'))

            return {
                'predictions': features_df.to_dict('records')
            }

        except TypeError as e:
            logging.error(e)
            raise TypeError(e)

        except Exception as e:
            logging.error(f'Error by getting predictions: {e}')
            raise Exception(e)

        finally:
            await csv_file.close()
