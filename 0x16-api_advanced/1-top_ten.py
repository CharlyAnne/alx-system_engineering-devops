#!/usr/bin/python3
"""Script prints the title of subreddits using reddit API endpoint"""
from requests import get


def top_ten(subreddit):
    """
    Function requests reddit api and returns the first 10 subreddit
    titles
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}

    response = get(url, headers=user_agent, params=params)
    resData = response.json()

    try:
        my_data = resData.get('data').get('children')

        for post in my_data:
            print(post.get('data').get('title'))

    except Exception:
        print("None")
