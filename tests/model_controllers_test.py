import pandas as pd
from typing import Dict

from backend_app.src.controllers.model_controller import ModelController
from backend_app.src.schemas.iris_input import IrisInput
from backend_app.src.schemas.iris_response import IrisResponse

IRIS_INPUT_MOCK: IrisInput = IrisInput(
    sepal_length = 1.0,
    sepal_width = 1.0,
    petal_length = 1.0,
    petal_width = 1.0,
)

class ModelTest:
    def __init__(self, n: int) -> None:
        self.__n = n

    def predict(self, _: pd.DataFrame):
        return [1]*self.__n

model_controller = ModelController(model=ModelTest())

def predict_test():
    model_controller.predict(IRIS_INPUT_MOCK)

    prediction = model_controller.predict(IRIS_INPUT_MOCK)

    expected = {
        'prediction': {IRIS_INPUT_MOCK.model_dump() | 'prediction': 0}
    }

    assert prediction == expected
