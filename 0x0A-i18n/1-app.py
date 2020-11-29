#!/usr/bin/env python3
""" Basic Flask app module.
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

@app.route('/')
def hello():
    """ Hello methtod.
    """
    return render_template('0-index.html')
