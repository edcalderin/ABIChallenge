from contextlib import asynccontextmanager
from fastapi import FastAPI, File, UploadFile
import logging
import uvicorn

from backend_app.src.controllers.singleton_model_controller import SingletonModelController
from backend_app.src.schemas.iris_input import IrisInput
from backend_app.src.utils import Utils

logging.basicConfig(level = logging.INFO, format = '%(asctime)s %(levelname)s %(message)s')

resource = dict()
   
@asynccontextmanager
async def app_lifestpan(_: FastAPI):
    '''
    Loading the model in the application startup, just at the first time
    '''
    logging.info('Loading model')
    resource['model'] = Utils.load_model()
    yield
    resource.clear()

app = FastAPI(lifespan = app_lifestpan)

@app.post('/predict')
def predict(input: IrisInput):
    controller = SingletonModelController(model = resource.get('model'))
    return controller.predict(input)

@app.post('/predict-batch')
async def predict_on_batch(csv_file: UploadFile = File(description='CSV File with Iris samples')):
    controller = SingletonModelController(model = resource.get('model'))
    return await controller.predict_on_batch(csv_file)

if __name__ == '__main__':
    uvicorn.run(app)