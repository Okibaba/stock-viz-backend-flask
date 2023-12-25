from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask import Blueprint, jsonify, request, render_template
from ..models import Stock, db


bp = Blueprint('stocks', __name__, url_prefix='/stocks')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    stocks = Stock.query.all()  # ORM performs SELECT query
    return render_template('stock_table_index.html', stocks=stocks)
    # result = []
    # for stock in stocks:
    #     # build list of stocks as dictionaries
    #     result.append(stock.serialize())
    # return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    stock = Stock.query.get_or_404(id, "stock not found")
    return jsonify(stock.serialize())


@bp.route('', methods=['POST'])
def create():
    # def __init__(self, stock_symbol: str, company_name: str, company_description: str):
    # self.stock_symbol = stock_symbol
    # self.company_name = company_name
    # self.company_description = company_description

    data = request.get_json()
    # req body must contain  stock_symbol
    if 'stock_symbol' not in data or 'company_name' not in data:
        missing_fields = [field for field in [
            'stock_symbol', 'company_name'] if field not in data]
        return jsonify({"error": f"Missing required field(s): {', '.join(missing_fields)}"}), 400

    data.setdefault('company_description', '')

    # Create new Stock instance
    try:
        stock = Stock(stock_symbol=data['stock_symbol'],
                      company_name=data['company_name'], company_description=data['company_description'])
        db.session.add(stock)
        db.session.commit()
        return jsonify(stock.serialize()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Data integrity issue"}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    stock = Stock.query.get_or_404(id, "stock not found")
    try:
        db.session.delete(stock)
        db.session.commit()
        return jsonify({"message": "Stock deleted successfully"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
