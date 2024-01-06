import logging
import pandas as pd
from typing import Dict, List

from backend_app.src.schemas.iris_input import IrisInput

class ModelController:
    
    def __init__(self, model) -> None:
        self.model = model
    
    def predict(self, input: IrisInput) -> Dict[str, int]:
        try:
            processed_input = pd.DataFrame(input.model_dump(), index = [0])
            prediction = self.model.predict(processed_input)[0]

        except Exception as e:
            logging.error(f'Unexpected error: {e}')
        
        else:
            return {
                'prediction': int(prediction)
            }
    