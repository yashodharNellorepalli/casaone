from app import db


class Rating(db.Model):
    __tablename__ = 'ratings'
    product_id = db.Column(db.String(255), primary_key=True)
    order_id = db.Column(db.String(255), primary_key=True)
    rating = db.Column(db.Integer)


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, autoincrement=True)
    mobile = db.Column(db.String(10), primary_key=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(100))


class City(db.Model):
    __tablename__ = 'cities'
    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100))


class Hub(db.Model):
    __tablename__ = 'hubs'
    hub_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100))
    city_id = db.Column(db.Integer, db.ForeignKey('City.city_id'))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)


class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    hub_id = db.Column(db.Integer, db.ForeignKey('Hub.hub_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))


class OrderItem(db.Model):
    __tablename__ = 'order_items'
    order_id = db.Column(db.Integer, db.ForeignKey('Order.order_id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.product_id'), primary_key=True)
    rent_from = db.Column(db.DateTime)
    rent_to = db.Column(db.DateTime)


class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.text)


class ProductMerchandising(db.Model):
    __tablename__ = 'product_merchandising'
    product_id = db.Column(db.Integer, db.ForeignKey('Product.product_id'), primary_key=True)
    hub_id = db.Column(db.Integer, db.ForeignKey('Hub.hub_id'), primary_key=True)
    price = db.Column(db.Float)
    color = db.Column(db.String)
    cost_of_assemble = db.Column(db.Float)
    time_to_assemble = db.Column(db.Integer)
