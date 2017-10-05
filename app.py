from flask  import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:youngmoney@localhost:5432/yummyrecipes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


db = SQLAlchemy(app)

class User(db.Model):
    """Model for storing User details"""
    userid = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column (db.String(50))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))


class Recipe(db.Model):
    """Model for storing recipe details"""
    recipe_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(140))

@app.route('/user', methods=['POST'])
def register_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method = 'sha256')
    new_user = User(public_id=str(uuid.uuid4()), name =data['name'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user has been registered'})



if __name__ == '__main__':
    app.run(debug=True)