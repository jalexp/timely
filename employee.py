from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site2.db'

db = SQLAlchemy(app)

class Employee(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=True, nullable=False)

	email = db.Column(db.String(20), unique=True, nullable=False)

	def __repr__(self):
		return f"Employee('{self.name}', '{self.email}')"
	
