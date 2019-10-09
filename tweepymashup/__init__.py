# Tweepy
# Copyright 2009-2019 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy Twitter API library
"""
__version__ = '1.0.7'
__author__ = ' oblockton - Joshua Roesslein'
__license__ = 'MIT'

from tweepymashup.api import API
from tweepymashup.auth import AppAuthHandler, OAuthHandler
from tweepymashup.cache import Cache, FileCache, MemoryCache
from tweepymashup.cursor import Cursor
from tweepymashup.error import RateLimitError, TweepError
from tweepymashup.models import DirectMessage, Friendship, ModelFactory, SavedSearch, SearchResults, Status, User
from tweepymashup.streaming import Stream, StreamListener

# Global, unauthenticated instance of API
api = API()

def debug(enable=True, level=1):
    from six.moves.http_client import HTTPConnection
    HTTPConnection.debuglevel = level
