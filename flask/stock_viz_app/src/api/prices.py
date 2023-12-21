from flask import Blueprint, jsonify, request
from ..models import Price, Stock, db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

bp = Blueprint('prices', __name__, url_prefix='/prices')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    prices = Price.query.all()  # ORM performs SELECT query
    result = []
    for price in prices:
        # build list of prices as dictionaries
        result.append(price.serialize())
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    price = Price.query.get_or_404(id, "Price not found")
    return jsonify(price.serialize())


@bp.route('', methods=['POST'])
def create():

    data = request.get_json()
    # req body must contain  stock_id
    if 'stock_id' not in data:
        return jsonify({"error": "'stock_id' is required"}), 400

    # Validate 'current_price' in data
    if 'current_price' not in data:
        return jsonify({"error": "'current_price' is required"}), 400

    # check for existence of stock with id of stock_id
    Stock.query.get_or_404(request.json['stock_id'], "Stock not found")
    # construct Price

    # Create new Price instance
    try:
        price = Price(stock_id=data['stock_id'],
                      current_price=data['current_price'])
        db.session.add(price)
        db.session.commit()
        return jsonify(price.serialize()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Data integrity issue"}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    price = Price.query.get_or_404(id, "Price for stock not found")
    try:
        db.session.delete(price)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)
