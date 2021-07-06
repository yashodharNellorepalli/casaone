from flask import jsonify, current_app

from app import app

from app.utils.constants import FAILURE_RESPONSE


@app.errorhandler(404)
def not_found_error(error):
    current_app.logger.error(error)
    response_data = {
        'message': str(error),
        'status': FAILURE_RESPONSE
    }

    return jsonify(response_data), 404


@app.errorhandler(500)
def internal_error(error):
    current_app.logger.error(error)
    response_data = {
        'message': str(error),
        'status': FAILURE_RESPONSE
    }

    return jsonify(response_data), 500
