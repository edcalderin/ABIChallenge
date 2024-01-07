from backend_app.src.controllers.model_controller import ModelController

class SingletonModelController:
    '''
    In order to avoid create muliple instances of the Model controller class, 
    a singleton class will be created to ensure that just one instance to be needed.
    '''
    
    model_controller = None
    
    def __new__(cls, model) -> ModelController:
        if cls.model_controller is None:
            cls.model_controller = ModelController(model = model)
            return cls.model_controller
        return cls.model_controller