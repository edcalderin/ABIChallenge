from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from backend_app.src.schemas.iris_input import IrisInput
from backend_app.src.controllers.model_controller import ModelController
from backend_app.src.utils import Utils
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

resource = {}

@asynccontextmanager
async def app_lifestpan(_: FastAPI):
    logging.info('Loading model')
    resource['model'] = Utils.load_model()
    yield
    resource.clear()

app = FastAPI(lifespan = app_lifestpan)

@app.post('/predict')
def predict(input: IrisInput):
    try:
        controller = ModelController(model = resource['model'])
        return controller.predict(input)
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    uvicorn.run(app)