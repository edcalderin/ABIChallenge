from typing import List

from pydantic import BaseModel
from backend_app.src.schemas.iris_input import IrisInput

class IrisResponse(IrisInput):
    prediction: int
