import logging
from fastapi import UploadFile
import pandas as pd
from typing import Dict, List
import csv
from io import StringIO

from backend_app.src.schemas.iris_input import IrisInput
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
            processed_input = pd.DataFrame(input.model_dump(), index = [0])
            prediction = self.__model.predict(processed_input)[0]
            prediction = int(prediction)

            item: Dict = input.model_dump()
            item['prediction'] = prediction

            self.__prediction_service.insert_one_prediction(item)
            return {
                'prediction': prediction
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
                yield record
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
    
    async def predict_on_batch(self, csv_file: UploadFile) -> Dict[str, List[int]]:
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
            records = [record async for record in self.__csv_reader(csv_file)]
        
            records = pd.DataFrame.from_records(records)

            predictions = self.__model.predict(records)
            
            # Parsing predictions to a native python data type
            return {
                'predictions': list(map(int, predictions))
            }

        except TypeError as e:
            logging.error(e)
            raise TypeError(e)

        except Exception as e:
            logging.error(f'Error by getting predictions: {e}')
            raise Exception(e)

        finally:
            await csv_file.close()
            