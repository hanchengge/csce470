#!/usr/bin/env python
# script to test your index and search engine
#
# You should add tests here, but you should not remove any of the tests in
# this file.

import unittest

import tweetsearch
import utils
from settings import settings


tiny_corpus = [
    dict(id=3,text="spade spade spade heart diamond"),
    dict(id=4,text="spade club"),
    dict(id=5,text="spade spade heart heart"),
    dict(id=6,text="club heart heart"),
]

class MockPageRanker(object):
    """
    MockPageRanker has the same interface as the PageRanker class, but it has a
    much simpler implementation. You can use this to check that tweetsearch uses
    the ranker correctly. When you use this ranker, tweets with the lowest id
    should come first in search results.
    """
    def rank(self,tweet):
        return 1.0/tweet['id']

class TestTokenize(unittest.TestCase):

    def test_tokenize(self):
        tokens = tweetsearch.tokenize("Info retrieval")
        self.assertEqual(tokens,['info','retriev'])

        tokens = tweetsearch.tokenize("Don't give up!")
        self.assertEqual(tokens,["don't",'give','up'])


class TestSearch(unittest.TestCase):
    def setUp(self):
        # this method runs before each test
        db = utils.connect_db('msl_unittest', remove_existing=True)
        ranker = MockPageRanker()
        self.ts = tweetsearch.TweetSearch(db,ranker)
        self.ts.index_tweets(iter(tiny_corpus))

    def test_can_follow_directions(self):
        # You need to change these fields in settings.py .
        self.assertNotEqual(settings['author'],'CSCE 470 Student')
        self.assertNotEqual(settings['uin'],'000-00-0000')
        self.assertTrue(settings['agree_to_honor_code'])

    def _assert_search(self, query, expected):
        docs = self.ts.search_results(query)
        # since order doesn't matter sort the ids
        ids = sorted(doc['id'] for doc in docs)
        self.assertEqual(ids,sorted(expected))

    def test_simple_search(self):
        self._assert_search('spade',[3,4,5])
        self._assert_search('spade club',[4])

    def test_bogus_search(self):
        self._assert_search('',[])
        self._assert_search('joker',[])

    # Add more tests here.

if __name__ == '__main__':
    unittest.main()
