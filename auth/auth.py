from ..app import app, VERSION

SERVICE_NAME = "auth"
prefix = "/".join(["", SERVICE_NAME, VERSION])

@app.route("/".join(prefix, "get_auth"))
def get_auth():
    return "get_auth"
