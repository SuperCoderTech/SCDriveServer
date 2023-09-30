from datetime import datetime
from functools import wraps

import jwt
from flask import Flask, request, jsonify, make_response
# to avoid cors error in different frontend like react js or any other
from flask_cors import CORS
import dns.resolver

from authentication import encode_auth_token
from image_controller import image_con
from folder_controller import folder_con
import thumbnailcreator
from image_handler import UPLOAD_FOLDER, set_upload_folder

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

app = Flask(__name__)
app.register_blueprint(image_con)
app.register_blueprint(folder_con)

# app.register_blueprint(profile)
app.config['secret_key'] = "4575efa590f470f95173ba50e9bf6f2f9aa1fb66fb74e3d2"
CORS(app)


@app.route("/")
def launch():
    return "launch success"


@app.route("/test")
def test():
    return "test"


@app.route("/thumb/<username>")
def thumb(username):
    thumbnailcreator.create_thumbnail_for_all(username)
    return "done"


@app.route("/getAuthToken/<username>")
def getAuthToken(username):
    token = encode_auth_token({"name": "Mr.B", "upath": username})
    print("token : " + token)
    return {"token": token}


@app.route("/change_upload_folder")
def change_upload_folder():
    folder = request.args["drive"]
    set_upload_folder('/home/dietpi/'+folder)
    print(UPLOAD_FOLDER)
    return {"status": UPLOAD_FOLDER}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
