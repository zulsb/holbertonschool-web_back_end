#!/usr/bin/env python3
""" App module.
"""
from auth import Auth
from flask import Flask, jsonify, request, abort, redirect

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def messageWelcome() -> str:
    """ Return a JSON payload of the form.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def registerUser() -> str:
    """ Method to register a user.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": "{}".format(user.email),
                        "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def log_in() -> str:
    """ Method that login.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password or not AUTH.valid_login(email, password):
        abort(401)
    
    newSession = AUTH.create_session(email)
    log = jsonify({"email": email, "message": "logged in"})
    log.set_cookie("session_id", newSession)
    return log


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """ Method that logout.
    """
    sessionId = request.cookies.get('session_id')

    if sessionId:
        user = AUTH.get_user_from_session_id(sessionId)
        if user:
            AUTH.destroy_session(user.id)
            return redirect("http://0.0.0.0:5000/")
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
