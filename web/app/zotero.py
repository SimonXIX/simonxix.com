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
import random
import gc

def get_publications():
    #get variables from config file
    library_id = os.environ.get('LIBRARY_ID')
    api_key = os.environ.get('API_KEY')

    zot = zotero.Zotero(library_id, 'user', api_key)
    return zot

def get_culture_items():
    zot = get_publications()
    publications = zot.publications(itemType='-attachment', tag='culture', content='bib', sort='date', style='modern-humanities-research-association-author-date', linkwrap=1)
    
    del zot
    gc.collect()

    return publications

def get_development_items():
    zot = get_publications()
    publications = zot.publications(itemType='-attachment', tag='development', content='bib', sort='date', style='modern-humanities-research-association-author-date', linkwrap=1)
    
    del zot
    gc.collect()

    return publications

def get_fiction_items():
    zot = get_publications()
    publications = zot.publications(itemType='-attachment', tag='fiction', content='bib', sort='date', style='modern-humanities-research-association-author-date', linkwrap=1)

    del zot
    gc.collect()

    return publications

def get_library_items():
    zot = get_publications()
    publications = zot.publications(itemType='-attachment', tag='library', content='bib', sort='date', style='modern-humanities-research-association-author-date', linkwrap=1)

    del zot
    gc.collect()

    return publications

def get_podcast_items():
    zot = get_publications()
    publications = zot.publications(itemType='podcast', content='bib', sort='extra', direction='desc', style='modern-humanities-research-association-author-date', linkwrap=1)

    del zot
    gc.collect()

    return publications

def get_film_reviews():
    #get variables from config file
    group_id = os.environ.get('GROUP_ID')
    api_key = os.environ.get('API_KEY')

    zot = zotero.Zotero(group_id, 'group', api_key)

    items = zot.items(itemType='-attachment')

    random.shuffle(items)

    reviews=[]

    for item in items[:10]:
        review = {}
        review['title'] = item['data']['title']
        review['link'] = item['data']['url']
        review['date'] = item['data']['extra']
        reviews.append(review)

    del zot
    del items
    gc.collect()

    return reviews