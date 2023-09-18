from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from db import db
from app.users.resources import UserRegistration, UserLogin
from app.bills.resources import BillResource, UpcomingBillResource
from app.settings import JWT_SECRET_KEY

def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql+psycopg2:///billz"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
    JWTManager(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    api.add_resource(UserRegistration, "/users/register")
    api.add_resource(UserLogin, "/users/login")
    api.add_resource(BillResource, "/bills", "/bills/<uuid:pk>")
    api.add_resource(UpcomingBillResource, "/upcoming-bills",
                     "/upcoming-bills/<uuid:pk>")

    return app

app=create_app()
if __name__ == "__main__":
    app.run(debug=True, port=8080)