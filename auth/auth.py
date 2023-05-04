from flask import Blueprint, request, jsonify
from conf import *
from models.users import *

auth = Blueprint('auth', __name__)
prefix = "/".join(["", "api", VERSION, "auth"])


@auth.route("/".join([prefix, "signup"]), methods=['POST'])
def auth_signup():
    request_data = request.json
    if not request_data.get("login"):
        return jsonify({'status': 'error', 'description': "The login field is blank", 'access_token': None})
    elif not request_data.get("password"):
        return jsonify({'status': 'error', 'description': "The password field is blank", 'access_token': None})
    elif not request_data.get("email"):
        return jsonify({'status': 'error', 'description': "The email field is blank", 'access_token': None})
    else:
        user = User(**request_data)
        session.add(user)
        session.commit()
        return jsonify({'status': 'success', 'description': "Successfully created!", 'access_token': user.get_token()})


@auth.route("/".join([prefix, "signin"]), methods=['POST'])
def auth_signin():
    request_data = request.json
    try:
        user = User.authenticate(**request_data)
        return jsonify({'status': 'success', 'description': "Successfully authenticated!", 'access_token': user.get_token()})
    except Exception as e:
        return jsonify({'status': 'error', 'description': f"Authentication failed: {str(e)}"})



def test_print():
    print("/".join([prefix, "signup"]))

# auth_token = HTTPTokenAuth(scheme='Bearer')
# auth_login = HTTPBasicAuth()


