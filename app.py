from flask import Flask, render_template, request, url_for, redirect, flash
from flask_bootstrap import Bootstrap

from controllers.class_room_controller import class_room_bp
from controllers.home_controller import home_bp
from models import db

app = Flask(__name__)

app.config["SECRET_KEY"] = "hello_world"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://minhduc@localhost/minhduc"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()

Bootstrap(app)

app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(class_room_bp, url_prefix='/class_room')

if __name__ == "__main__":
    app.run(debug=True)
