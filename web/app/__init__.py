# @name: __init__.py
# @version: 0.1
# @creation_date: 2022-08-25
# @license: The MIT License <https://opensource.org/licenses/MIT>
# @author: Simon Bowie <simon.bowie.19@gmail.com>
# @purpose: Initialises the app
# @acknowledgements:

from flask import Flask, render_template, request
from flask_moment import Moment
import requests
import markdown

# initiate Moment for datetime functions
moment = Moment()

app = Flask(__name__)

moment.init_app(app)

@app.route('/')
def index():
    with open('content/home.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    return render_template('index.html', html=html)

@app.route('/critic')
def critic():
    with open('content/critic.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    return render_template('critic.html', html=html)

@app.route('/developer')
def developer():
    with open('content/developer.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    return render_template('developer.html', html=html)

@app.route('/photographer')
def photographer():
    with open('content/photographer.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    return render_template('photographer.html', html=html)

@app.route('/podcaster')
def podcaster():
    with open('content/podcaster.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    return render_template('podcaster.html', html=html)
