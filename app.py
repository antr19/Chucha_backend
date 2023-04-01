from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import models.users


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    # blueprint for auth routes in our app
    from auth.auth import auth, test_print
    test_print()
    app.register_blueprint(auth)

    return app


app = create_app()
client = app.test_client()
jwt = JWTManager(app)


@app.route("/")
def hello_world():
    return "Sorry, maaaan..."


