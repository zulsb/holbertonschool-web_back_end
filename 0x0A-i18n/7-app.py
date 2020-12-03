#!/usr/bin/env python3
""" Basic Flask app module.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from pytz import timezone, exceptions

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Language and time zone settings.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)


def get_user():
    """ Method that returns a user dictionary or None if the ID
        cannot be found.
    """
    try:
        return users.get(int(request.args.get("login_as")))
    except Exception:
        return None


@app.before_request
def before_request():
    """ before request
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ Method to determine the best match with our supported languages.
    """
    local = request.args.get('locale')
    if local and local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Method that deduces the proper time zone.
    """
    log = get_user()
    if log:
        locale = log['timezone']
    if request.args.get('timezone'):
        locale = request.args.get('timezone')
    try:
        return timezone(locale).zone
    except Exception:
        return None


@app.route('/')
def hello():
    """ Hello method.
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
