from flask import Blueprint, request
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from conf import *
from models.users import *

auth = Blueprint('auth', __name__)
prefix = "/".join(["", "api", VERSION, "auth"])


@auth.route("/".join([prefix, "signup"]))
def auth_signup():
    request_data = request.get_json()
    if not request_data.get("login"):
        return "Error login"
    elif not request_data.get("password"):
        return "Error password"
    elif not request_data.get("email"):
        return "Error email"
    else:
        query = User(
            login=request_data.get("login"),
            password=request_data.get("password"),
            email=request_data.get("email")
        )
        session.add(query)
        session.commit()
        return "True"


def test_print():
    print("/".join([prefix, "signup"]))

# auth_token = HTTPTokenAuth(scheme='Bearer')
# auth_login = HTTPBasicAuth()



# tokens = {
#     "secret-token-1": "john",
#     "secret-token-2": "susan"
# }
#
# @auth_token.verify_token
# def verify_token(token):
#     if token in tokens:
#         return tokens[token]


# @auth_login.get_password
# def get_password(username):
#     request_data = request.get_json() # only post?
#     if username == 'miguel':
#         return 'python'
#     return None



# @app.route("/".join([prefix, "auth"]))
# @auth_login.login_required
# def get_auth():
#     return "get_auth"
