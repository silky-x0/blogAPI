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

@app.route("/")
def home():
    return '<h1>Hello wrld</h1>'

@app.route("/user")
def ppl():
    return "Hello ppl"

if __name__ == "__main__":
    app.run(debug=True)

