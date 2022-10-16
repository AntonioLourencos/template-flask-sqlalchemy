import os

# Lib
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from dotenv import load_dotenv

# Meu models
from config.database import db
from models.users import Users

load_dotenv()
app = Flask(__name__)

# Configurar BD
FULL_URL_DB = f'postgresql://{os.environ.get("USER_DB")}:{os.environ.get("PASS_DB")}@{os.environ.get("URL_DB")}/{os.environ.get("NAME_DB")}'
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'ChaveSecreta'
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)


@app.route('/', methods=['GET'])
def index():
    users = Users.query.all()
    users = [user.to_json() for user in users]
    countUsers = Users.query.count()

    return jsonify({"message": "Sucess!!", "Quantity": countUsers, "users": users})


@app.route('/<int:id>', methods=['GET'])
def getOneById(id):
    user = Users.query.get_or_404(id)
    user = user.to_json()

    return jsonify({"message": "Sucess!!", "user": user})


@app.route('/create', methods=['POST'])
def create():
    dataUser = request.get_json()
    user = Users(dataUser['name'], dataUser['email'], dataUser['password'])
    db.session.add(user)
    db.session.commit()
    return {"message": "Sucess!!"}


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    user = Users.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return {"message": "Sucess!!"}


@app.route('/updateName/<int:id>', methods=['PUT'])
def update(id):
    user = Users.query.get_or_404(id)
    dataUser = request.get_json()

    if dataUser['name']:
        user.name = dataUser['name']
        db.session.commit()

    return {"message": "Sucess!!"}


def Merge(dict1, dict2):
    return (dict1.update(dict2))


if __name__ == '__main__':
    app.run(debug=True)
