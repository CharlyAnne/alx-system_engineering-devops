#!/usr/bin/python3
"""Script queries the Reddit api for a list containing titles"""
import requests


def recurse(subreddit, count=0, after=None, hot_list=[]):
    """
    function queries the Reddit API recursively and returns a list
    of all hot article titles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "count": count, "after": after}
    headers = {"User-Agent": "Google Chrome Version 81.0.4044.129"}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()
    resData = data.get('data').get('children')
    afterData = data.get('data').get('after')

    if not resData:
        if count == 0:
            return None
        else:
            return hot_list

    for post in resData:
        hot_list.append(post.get('data').get('title'))

    return recurse(subreddit, count=count+100, after=afterData,
                   hot_list=hot_list)
