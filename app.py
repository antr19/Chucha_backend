from flask import Flask
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


@app.route("/")
def hello_world():
    return "Sorry, maaaan..."


