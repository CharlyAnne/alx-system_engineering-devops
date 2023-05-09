#!/usr/bin/python3
"""Script prints the title of subreddits using reddit API endpoint"""
import requests


def top_ten(subreddit):
    """
    Function requests reddit api and returns the
    first 10 subreddit titles
    """
    baseUrl = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Google Chrome Version 81.0.4044.129"}
    params = {"limit": 10}
    
    response = get(baseUrl, headers=user_agent, params=params)
    resData = response.json()

    try:
        response = resData.get("data").get("children")

        for post in response:
            print(post.get("data").get("title"))

    except Exception:
        print("None")
