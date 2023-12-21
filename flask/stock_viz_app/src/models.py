import datetime
from decimal import Decimal
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_symbol = db.Column(db.String(128), unique=True, nullable=False)
    company_name = db.Column(db.String(128), unique=True, nullable=False)
    company_description = db.Column(db.String(128), default='')
    prices = db.relationship('Price', backref='stock',
                             cascade="all, delete", lazy=True)

    def __init__(self, stock_symbol: str, company_name: str, company_description: str):
        self.stock_symbol = stock_symbol
        self.company_name = company_name
        self.company_description = company_description

    def serialize(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'stock_symbol': self.stock_symbol,
            'company_description': self.company_description

        }


class Price(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time_stamp = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    current_price = db.Column(db.Numeric)
    stock_id = db.Column(db.Integer, db.ForeignKey(
        'stocks.id'), nullable=False)

    def __init__(self, current_price: Decimal, stock_id: int):
        self.current_price = current_price
        self.stock_id = stock_id

    def serialize(self):
        return {
            'id': self.id,
            'time_stamp': self.time_stamp.isoformat() if self.time_stamp else None,
            'current_price': str(self.current_price) if self.current_price is not None else None,
            'stock_id': self.stock_id
        }
