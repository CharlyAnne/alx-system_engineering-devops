#!/usr/bin/python3
""" Script to query an API and return value """

from requests import get


def number_of_subscribers(subreddit):
    """
     function request Reddit API and returns the number of
     subscribers for a given subreddit.
     """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    resData = response.json()

    try:
        return resData.get('data').get('subscribers')

    except Exception:
        return 0
