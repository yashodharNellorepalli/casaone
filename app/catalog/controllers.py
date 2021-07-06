from flask import Blueprint, jsonify, request

from app.utils.constants import HTTP_200_OK, HTTP_500_INTERNAL_ERROR
from app.utils.constants import SUCCESS_RESPONSE, FAILURE_RESPONSE
from app.catalog.service import get_product_rating

catalog_module = Blueprint('catalog', __name__, url_prefix='/catalog')


@catalog_module.route('/get-rating', methods=['GET'])
def get_rating():
    try:
        request_data = request.args
        product_id = request_data.get('product_id')
        response = get_product_rating(product_id)
        return jsonify({
            'status': SUCCESS_RESPONSE,
            'data': response
        }), HTTP_200_OK
    except Exception as e:
        return jsonify({'message': str(e), 'status': FAILURE_RESPONSE}), HTTP_500_INTERNAL_ERROR
