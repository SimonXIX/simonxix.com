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
import re
from . import zotero

# initiate Moment for datetime functions
moment = Moment()

app = Flask(__name__)

moment.init_app(app)

@app.context_processor
def get_onion():
    with open('content/onion.md', 'r') as f:
        onion = f.read()
    return dict(onion=onion)

@app.route('/')
def index():
    with open('content/home.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    with open('content/onion.md', 'r') as f:
        onion = f.read()

    return render_template('index.html', html=html, onion=onion)

@app.route('/contact')
def contact():
    with open('content/contact.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    return render_template('contact.html', html=html)

@app.route('/critic')
def critic():
    with open('content/critic.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    items = zotero.get_culture_items()

    fictions = zotero.get_fiction_items()

    return render_template('critic.html', html=html, items=items, fictions=fictions)

@app.route('/developer')
def developer():
    with open('content/onion.md', 'r') as f:
        onion = f.read()

    with open('content/developer.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
        pattern = 'ONION_ADDRESS'
        html = re.sub(pattern, onion, html)

    items = zotero.get_development_items()

    return render_template('developer.html', html=html, items=items)

@app.route('/librarian')
def librarian():
    with open('content/librarian.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    items = zotero.get_library_items()

    return render_template('librarian.html', html=html, items=items)

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

    items = zotero.get_podcast_items()

    return render_template('podcaster.html', html=html, items=items)
