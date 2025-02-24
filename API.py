from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse.db'
db = SQLAlchemy(app)
api = Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Uname = db.Column(db.String(80), unique = True, nullable = False)
    mail = db.Column(db.String(80), unique = True, nullable = False)

    def __repr__(self):
        return f"Username = {self.Uname}, Email = {self.mail}"

user_args = reqparse.RequestParser()
user_args.add_argument('Uname', type=str, required=True, help="Name cannot be empty")
user_args.add_argument('mail', type=str, required=True, help="mail cannot be empty")

userFields = {
    'id':fields.Integer,
    'Uname':fields.String,
    'mail':fields.String,
}
class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users
    
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(Uname=args["Uname"], mail=args["mail"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201

api.add_resource(Users, '/api/users')    

@app.route("/")
def home():
    return '<h1>Hello wrld</h1>'



if __name__ == "__main__":
    app.run(debug=True)

