import os.path
import sys
import pkgutil

from application import controllers
from application.models import init_model
from config import environments

__all__ = ['InvalidEnvironmentError', 'ConfigMiddleware', 'ControllerMiddleware']

class InvalidEnvironmentError(Exception):
    message = "Invalid environment name. Please use one of the following: [" + ",".join(environments.keys()) + "]"

def ConfigMiddleware(app, environment):
    if not environments.get(environment):
        raise InvalidEnvironmentError()
    
    app.config.from_object(environments[environment])
    db_uri = app.config.get('DB_URI')
    init_model(db_uri)
    return app

def ControllerMiddleware(app):
    
    pkg_path = os.path.dirname(controllers.__file__)
    
    controller_names = [name for _, name, _ in pkgutil.iter_modules([pkg_path])]
    for controller_name in controller_names:
	qualified_name = controllers.__name__ + '.' + controller_name
        __import__(qualified_name)
        controller = sys.modules[qualified_name]
        module_name = controller.__name__.split('.')[-1]
        # Each controller should have an attribute of the same name
        # to declare a Flask Module
        flask_module = getattr(controller, module_name)
        app.register_module(flask_module)
    return app
