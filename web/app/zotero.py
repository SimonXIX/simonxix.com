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

def get_library():
    #get variables from config file
    library_id = os.environ.get('LIBRARY_ID')
    api_key = os.environ.get('API_KEY')

    zot = zotero.Zotero(library_id, 'user', api_key)
    items = zot.top(limit=5)
    # we've retrieved the latest five top-level items in our library
    # we can print each item's item type and ID
    return items
