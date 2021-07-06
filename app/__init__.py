# Import flask and template operators
import os

import flask_monitoringdashboard as dashboard
from flask import Flask
from flask_compress import Compress
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.utils.constants import HTTP_401_UNAUTHORIZED, FAILURE_RESPONSE
from config import configure_app

# Application Definition
app = Flask(__name__,
            instance_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), '../instance'),
            instance_relative_config=True)
configure_app(app)
dashboard.bind(app)

cors = CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
Compress(app)

# Import errors
from app import errors

# Import a module / component using its blueprint handler variable (dispatch_module)
from app.catalog.controllers import catalog_module

# Import models

# Register blueprint(s)
app.register_blueprint(catalog_module)
