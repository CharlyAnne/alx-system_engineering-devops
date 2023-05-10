#!/usr/bin/python3
""" Script to query an API and return value """

from requests import get


def number_of_subscribers(subreddit):
    """
     function request Reddit API and returns the number of
     subscribers for a given subreddit.
     """
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    headers = {"User-Agent": "Google Chrome Version 81.0.4044.129"}
    subscribers = 0
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        subscribers = data["data"]["children"][1]["data"]["subreddit_subscribers"]
        return subscribers
    except requests.exceptions.HTTPError as error:
        return subscribers
