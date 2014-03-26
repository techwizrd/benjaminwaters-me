#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask import render_template
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/personal')
def personal():
    return render_template('personal.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True)')
