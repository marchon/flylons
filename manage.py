from flaskext.script import Manager, Server
from flask import Flask, Module

from application.config import config
from application.config.middleware import *
from application import app

manager = Manager(app)

@manager.command
def runserver(environment): 
    app = manager.app
    try:
        app = ConfigMiddleware(app, environment)
    except InvalidEnvironmentError as e:
        exit(e.message)    
    app = ControllerMiddleware(app)
    app.run()

if __name__ == '__main__':
    manager.run()
