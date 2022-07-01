from flask import Flask
from .routes import todo_blueprint
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.register_blueprint(todo_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)
