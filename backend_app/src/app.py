from fastapi import FastAPI
import uvicorn
from backend_app.src.schemas.iris_input import IrisInput
from backend_app.src.controllers.model_controller import ModelController

app = FastAPI()

@app.post('/predict')
def predict(input: IrisInput):
    controller = ModelController()
    return controller.predict(input)

if __name__ == '__main__':
    uvicorn.run(app)