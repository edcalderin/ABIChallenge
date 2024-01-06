from typing import Dict
import pandas as pd

from backend_app.src.schemas.iris_input import IrisInput
from backend_app.src.utils import Utils

class ModelController:
    
    def predict(self, input: IrisInput) -> Dict[str, float]:
        processed_input = pd.DataFrame(input.model_dump(), index = [0])
        model = Utils.load_model()
        prediction = model.predict(processed_input)[0]
    
        return {
            'prediction': int(prediction)
        }