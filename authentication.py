import datetime
from functools import wraps

import jwt
from flask import request, make_response, jsonify

from flask import current_app as app


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers
        if 'authKey' in request.args:
            token = request.args['authKey']
        if not token:  # throw error if no token provided
            return make_response(jsonify({"message": "A valid token is missing!"}), 401)
        try:
            data = jwt.decode(token, app.config.get('secret_key'), algorithms=['HS256'])
            user = data['user']
        except:
            return make_response(jsonify({"message": "Invalid token!"}), 401)
        return f(user, *args, **kwargs)

    return decorator


def encode_auth_token(user):
    """
    Generates the Auth Token
    :return: string
    """

    print("secret key ::" + app.config.get('secret_key'))
    print("user :: " + str(user))
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'user': user
        }

        print("payload ::" + str(payload))

        return jwt.encode(
            payload,
            app.config.get('secret_key'),
            algorithm='HS256'
        )
    except Exception as e:
        return e
