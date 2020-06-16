from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
password="Usharani@31"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://usharani:Usharani@31@localhost:5432/cars_api"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:{}@localhost:5432/cars_api".format(password)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres@localhost/cars_api'
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://usharani:%s@localhost:5432/cars_api"%parse.unquote_plus('badpass')
# engine = create_engine('postgres://user:%s@host/database' % parse.unquote_plus('badpass')
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"

