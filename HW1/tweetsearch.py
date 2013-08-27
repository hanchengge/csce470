from __future__ import division
import re


from stemming import porter2
from pymongo import ASCENDING, DESCENDING


def tokenize(text):
    """
    Take a string and split it into tokens on word boundaries.

    A token is defined to be one or more alphanumeric characters,
    underscores, or apostrophes.  Remove all other punctuation, whitespace, and
    empty tokens.  Do case-folding to make everything lowercase. This function
    should return a list of the tokens in the input string.
    """
    tokens = re.findall("[\w']+", text.lower())
    return [porter2.stem(token) for token in tokens]


class TweetSearch(object):
    """ A search engine for tweets. """
    def __init__(self, mongo, ranker=None, classifier=None):
        """
        purpose: Create the search engine for tweets
        parameters:
            mongo - the pymongo Database object
            ranker - an object that can determine the order of tweets
                     (for homework 4)
            classifier - an object that can classify tweets
                     (for homework 5)
        """
        # We only need one collection within the database.
        self.tweet_collection = mongo['tweet']
        # ranker will be None until homework 4
        self.ranker = ranker
        # classifier will be None until homework 5
        self.classifier = classifier

    def index_tweets(self,tweets):
        """
        purpose: read the tweet dicts and store them in the database
        preconditions: the database is empty
        parameters:
          tweets - an iterator of tweet dictionaries
        returns: none
        """
        for tweet in tweets:
            if self.classifier:
                tweet['sentiment'] = self.classifier.sentiment(tweet)
            doc = dict(
                tokens = list(set(tokenize(tweet['text']))),
                tweet = tweet,
                rank = self.ranker.rank(tweet) if self.ranker else 0
            )
            self.tweet_collection.insert(doc)

        self.tweet_collection.create_index(
            [('tokens',ASCENDING),('rank',DESCENDING)])

    def search_results(self, query):
        """
        purpose: searches for the terms in "query" in our corpus using logical
            AND. Put another way, it returns a list of all of the tweets that
            contain all of the terms in query.
        preconditions: index_tweets() has already processed the corpus
        parameters:
          query - a string of terms
        returns: list of dictionaries containing the tweets
        """
        tokens = tokenize(query)
        docs_ = self.tweet_collection.find( {'tokens':{'$all':tokens}} )
        docs = docs_.sort('rank',DESCENDING)
        return [doc['tweet'] for doc in docs[:100]]