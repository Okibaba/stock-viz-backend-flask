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

class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_id = db.Column(db.String(128), unique=True, nullable=False)
    symbol = db.Column(db.String(128), nullable=False)
    company_name = db.Column(db.String(128), nullable=False)
    company_description = db.Column(db.String(128), nullable=False)
    prices = db.relationship('Price', backref='Stock', cascade="all,delete")

    def __init__(self, symbol: str, company_name: str):
        self.symbol = symbol
        self.company_name = company_name

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username
        }
