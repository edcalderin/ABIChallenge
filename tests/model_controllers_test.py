import os
import pandas as pd

from backend_app.src.controllers.model_controller import ModelController
from backend_app.src.schemas.iris_input import IrisInput
from backend_app.src.schemas.iris_response import IrisResponse

IRIS_INPUT_MOCK: IrisInput = IrisInput(
    sepal_length = 1.0,
    sepal_width = 1.0,
    petal_length = 1.0,
    petal_width = 1.0
)

class ModelTest:
    def __init__(self, length: int) -> None:
        self.__length = length

    def predict(self, _: pd.DataFrame):
        return [1]*self.__length

os.environ['IS_TEST'] = 'True'


def test_predict():
    model_controller = ModelController(model = ModelTest(1))
    prediction = model_controller.predict(IRIS_INPUT_MOCK)

    expected = {
        'prediction': IrisResponse(**IRIS_INPUT_MOCK.model_dump() | {'prediction': 1})
    }

    assert prediction == expected