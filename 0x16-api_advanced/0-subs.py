#!/usr/bin/python3
""" Script to query an API and return value """

import requests
from requests import get


def number_of_subscribers(subreddit):
    """
     function queries the Reddit API and returns the number of subscribers
     for a given subreddit.
     """
