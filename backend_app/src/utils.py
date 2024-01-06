import pickle
import logging
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

class Utils:

    @staticmethod
    def load_model():
        try:
            MODEL_PATH: Path = ROOT_DIR.joinpath('iris_model.pkl')
            with open(MODEL_PATH, 'rb') as file:
                model_pkl = pickle.load(file)
            return model_pkl
    
        except FileNotFoundError as e:
            logging.error(f'The model {MODEL_PATH} was not found')
