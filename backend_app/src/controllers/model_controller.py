from contextlib import asynccontextmanager, contextmanager
import logging
from fastapi import UploadFile
import pandas as pd
from typing import Dict, List
import csv
from io import StringIO

from backend_app.src.schemas.iris_input import IrisInput

class ModelController:
    
    '''
    Class containing controllers methods for the endpoints.
    '''
    
    def __init__(self, model) -> None:
        self.__model = model
    
    def predict(self, input: IrisInput) -> Dict[str, int]:
        try:
            processed_input = pd.DataFrame(input.model_dump(), index = [0])
            prediction = self.__model.predict(processed_input)[0]
            return {
                'prediction': int(prediction)
            }

        except Exception as e:
            logging.error(f'Unexpected error: {e}')
        
    async def __csv_reader(self, csv_file: UploadFile):
        '''
        Yields a record from the csv file
        
        Parameters:
        csv_file: Csv file as UploadFile data type
        
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
        finally:
            buffer.close()
    
    async def predict_on_batch(self, csv_file: UploadFile):
        try:
            if not csv_file.content_type == 'text/csv':
                raise TypeError('Uploaded file is not a valid csv')
            
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

        except Exception as e:
            logging.error(f'Error by getting predictions: {e}')
        finally:
            await csv_file.close()
            