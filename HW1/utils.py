# Some helper functions.
# You should not need to edit this file.

import json
import fileinput

from pymongo import connection
from pymongo import mongo_client

from settings import settings


def read_tweets():
    for line in fileinput.input():
        yield json.loads(line)
	#print "The data has been read!" + line

def connect_db(dbname, remove_existing=False):
    #con = connection.Connection(settings['mongo_host'],settings['mongo_port'])
	con = mongo_client.MongoClient(settings['mongo_host'],settings['mongo_port'])
	if remove_existing:
		con.drop_database(dbname)
	return con[dbname]


