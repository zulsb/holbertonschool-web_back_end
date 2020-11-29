#!/usr/bin/env python3
""" Basic Flask app module.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    """ Hello methtod.
    """
    return render_template('0-index.html')
