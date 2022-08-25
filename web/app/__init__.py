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
import urllib.request, json

# initiate Moment for datetime functions
moment = Moment()

app = Flask(__name__)

moment.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')
