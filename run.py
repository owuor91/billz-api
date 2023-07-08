from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from db import db
from app.users.resources import UserRegistration, UserLogin

def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql+psycopg2:///billz"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "xQUwFkHeHWcP6BVE"
    JWTManager(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    api.add_resource(UserRegistration, "/users/register")
    api.add_resource(UserLogin, "/users/login")

    return app

app=create_app()
if __name__ == "__main__":
    app.run(debug=True, port=8080)