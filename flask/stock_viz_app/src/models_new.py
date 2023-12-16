import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# CREATE TABLE stocks (
#     id SERIAL,
#     stock_id TEXT UNIQUE NOT NULL,
#     symbol TEXT UNIQUE NOT NULL,
#     company_name TEXT,
#     company_description TEXT,
#     PRIMARY KEY (id)
#     );

# to do:
# update types for table
# create apis
# create integrations with alembic
# test api with insomnia
# add html pages for displaying a few stocks and price on a table
# verify post is working locally on table
# verify delete is working on html table
# create a docker image
# run from the cloud

class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_symbol = db.Column(db.String(128), nullable=False)
    company_name = db.Column(db.String(128), nullable=False)
    company_description = db.Column(db.String(128), nullable=False)
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
            'stock_symbol': self.stock_symbol

        }


class Price(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time_stamp = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    current_price = db.Column(db.String(280), nullable=False)
    stocks_id = db.Column(db.Integer, db.ForeignKey(
        'stocks.id'), nullable=False)

    def __init__(self, current_price: str, stock_symbol: str):
        self.current_price = current_price
        self.stock_symbol = stock_symbol

    def serialize(self):
        return {
            'stock_symbol': self.id,
            'current_price': self.content,
            'time_stamp': self.time_stamp.isoformat(),
        }
