import json
import logging
from pathlib import Path
import pickle
import sys

ROOT_DIR = Path(__file__).parent.parent

class Utils:

    @staticmethod
    def load_model():
        try:
            MODEL_PATH: Path = ROOT_DIR.joinpath('iris_model.pkl')
            with open(MODEL_PATH, 'rb') as file:
                model_pkl = pickle.load(file)

        except FileNotFoundError as e:
            exc_type, _, exc_traceback = sys.exc_info()
            
            exception_details = {
                'exc_type': exc_type.__name__,
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'module': exc_traceback.tb_frame.f_code.co_name,
                'line_number': exc_traceback.tb_lineno,
                'exception': str(e)
            }
            
            logging.error(json.dumps(exception_details, indent = 3))
        
        except Exception as e:
            logging.error(e)
            
        else:
            return model_pkl