from datetime import datetime
from functools import wraps

import jwt
from flask import Flask, request, jsonify, make_response
# to avoid cors error in different frontend like react js or any other
from flask_cors import CORS
import dns.resolver

from authentication import encode_auth_token
from image_controller import image_con
import thumbnailcreator

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

app = Flask(__name__)
app.register_blueprint(image_con)
# app.register_blueprint(profile)
app.config['secret_key'] = "4575efa590f470f95173ba50e9bf6f2f9aa1fb66fb74e3d2"
CORS(app)


@app.route("/")
def launch():
    return "launch success"


@app.route("/test")
def test():
    return "test"


@app.route("/thumb")
def thumb():
    thumbnailcreator.create_thumbnail_for_all()
    return "done"


@app.route("/getAuthToken")
def getAuthToken():
    token = encode_auth_token({"name": "Mr.B", "upath": "MRB"})
    print("token : " + token)
    return {"token": token}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
