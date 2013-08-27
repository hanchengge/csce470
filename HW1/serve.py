#!/usr/bin/env python
# web server for tweet search
# You should not need to edit this file.

import time

import bottle
import tweetsearch
import utils
from settings import settings

_searcher = None

@bottle.route('/search')
def search(name='World'):
    global _searcher
    query = bottle.request.query.q
    start_time = time.time()
    tweets = _searcher.search_results(query)
    end_time = time.time()

    return dict(
            tweets = tweets,
            author = settings['author'],
            agree_to_honor_code = settings['agree_to_honor_code'],
            count = len(tweets),
            time = end_time - start_time,
            )


@bottle.route('/')
def index():
    return bottle.static_file('index.html', root='static')


@bottle.route('/favicon.ico')
def favicon():
    return bottle.static_file('favicon.ico', root='static')


@bottle.route('/static/<filename:path>')
def server_static(filename):
    return bottle.static_file(filename, root='static')


if __name__=="__main__":
	db = utils.connect_db('msl',True)
	_searcher = tweetsearch.TweetSearch(db)
	_searcher.index_tweets(utils.read_tweets())
	bottle.run(host=settings['http_host'],
               port=settings['http_port'],
               reloader=True)
