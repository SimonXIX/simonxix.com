# @name: zotero.py
# @version: 0.1
# @creation_date: 2022-08-25
# @license: The MIT License <https://opensource.org/licenses/MIT>
# @author: Simon Bowie <simon.bowie.19@gmail.com>
# @purpose: Performs Zotero functions
# @acknowledgements:
# Pyzotero: a Python client for the Zotero API: https://github.com/urschrei/pyzotero

from pyzotero import zotero
import os

def get_publications():
    #get variables from config file
    library_id = os.environ.get('LIBRARY_ID')
    api_key = os.environ.get('API_KEY')

    zot = zotero.Zotero(library_id, 'user', api_key)
    publications = zot.publications(itemType='-attachment', content='bib', sort='date', style='harvard-cite-them-right', linkwrap=1)
    return publications

def parse_publications():
    items = get_publications()

    #results = []
    #for item in items:
    #    if item['data']['itemType'] != 'attachment':
    #        results.append(item['data']['date'][:4] + ', ' + item['data']['title'])

    return items
