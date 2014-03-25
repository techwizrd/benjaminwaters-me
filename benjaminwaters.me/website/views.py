from flask import render_template
from website import website

@website.route('/')
def index():
    return render_template('index.html')
@website.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
