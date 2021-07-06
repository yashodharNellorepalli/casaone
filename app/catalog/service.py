from app.models.model import Rating
from app import db


def get_product_rating(product_id):
    average, count = db.session.query(
        db.func.avg(Rating.rating).label('Average'), db.func.count(Rating.rating).label('Count')
    )\
        .filter(Rating.product_id==product_id)\
        .first()

    return {
        'average': average,
        'count': count
    }
