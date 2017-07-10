# -*- encoding:utf-8 -*-
from flask import Flask, render_template, request
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)


# @app.route('/index/')
@app.route('/')
def index():
    return 'hello'


@app.route('/profile/<int:uid>/')
def profile(uid):
    colors = ('red', 'green')
    return render_template('profile.html', uid=uid, colors=colors)


@app.route('/request/')
def request_demo():
    res = ' '
    for property in dir(request):
        res = res + str(property) + '<br>' + str(eval('request.' + property)) + '<br>'
    return res


@app.route('/log/<level>/<msg>/')
def log(level, msg):
    dict = {'info': logging.INFO, 'warn': logging.WARN, 'error': logging.ERROR}
    if dict.has_key(level):
        app.logger.log(dict[level], msg)
        return 'logged:' + msg


def set_logger():
    info_file_handler = RotatingFileHandler('D:\\logs\\info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('D:\\logs\\warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('D:\\logs\\error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)


if __name__ == '__main__':
    set_logger()
    app.run(debug=True)
