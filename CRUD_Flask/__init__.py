from flask import Flask
from .views import crud_blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(crud_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)
