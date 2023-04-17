from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

import models.users
from auth.auth import auth, test_print
from swagger.swagger import swaggerui_blueprint


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    # blueprint for auth routes in our app
    test_print()
    app.register_blueprint(auth)
    app.register_blueprint(swaggerui_blueprint)

    return app


app = create_app()
client = app.test_client()
jwt = JWTManager(app)


@app.route("/")
def hello_world():
    return "Sorry, maaaan..."


