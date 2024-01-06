import json
import logging
from pathlib import Path
import pickle
import sys

ROOT_DIR = Path(__file__).parent.parent

class Utils:
    
    def __get_exc_info(self, exc):
        exc_type, _, exc_traceback = sys.exc_info()
            
        exception_details = {
            'exc_type': exc_type.__name__,
            'filename': exc_traceback.tb_frame.f_code.co_filename,
            'module': exc_traceback.tb_frame.f_code.co_name,
            'line_number': exc_traceback.tb_lineno,
            'exception': str(exc)
        }
        return json.dumps(exception_details, indent = 3)
    
    @classmethod
    def load_model(cls):
        try:
            MODEL_PATH: Path = ROOT_DIR.joinpath('iris_model.pkl')
            with open(MODEL_PATH, 'rb') as file:
                model_pkl = pickle.load(file)

        except FileNotFoundError as e:           
            logging.error(cls.__get_exc_info(cls, e))
            sys.exit()
    
        except Exception as e:
            logging.error(cls.__get_exc_info(cls, e))
            sys.exit()
            
        else:
            return model_pkl