"""Flask Api"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATA_URI'] ='postgresql://postgres:youngmoney@localhost:5432/yummyrecipes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

#Models

class Users(db.Model):
    """ User Model for storing user related details """
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))


class Recipes(db.Model):
    """ Recipe Model for storing Recipe details"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String())





if __name__ == '__main__':
    app.run(debug=True)



