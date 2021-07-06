# Define the application directory
import logging
import os


class BaseConfig(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # Logger configurations
    LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    # LOGGING_LOCATION = 'logs/application' + time.strftime("%Y-%m-%d") + ".log"
    LOGGING_LEVEL = logging.INFO


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    THREADS_PER_PAGE = 2
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Application threads.Just Like node JS Pm2 Clusters
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"


config = {
    "dev": "config.DevelopmentConfig",
    "staging": "config.StagingConfig",
    "prod": "config.ProductionConfig",
    "default": "config.DevelopmentConfig"
}


def configure_app(app):
    # If FLASK_CONFIGURATION variable is exported as a environment variable take its value or use default
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])

    # This file should be present inside the 'instance_path' location, containing the sensitive
    # information specific to env
    # app.config.from_pyfile('env.cfg', silent=True)
    app.config.from_pyfile('env_constants.py', silent=True)

    # Configure logging
    handler = logging.StreamHandler()  # logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    logger = logging.getLogger(__name__)
