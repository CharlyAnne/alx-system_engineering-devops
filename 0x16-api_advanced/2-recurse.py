#!/usr/bin/python3
"""Script queries the Reddit api for a list containing titles"""
import requests


def recurse(subreddit, count=0, after=None, hot_list=[]):
    """
    function queries the Reddit API recursively and returns a list of all 
    hot article titles for a given subreddit.
    """
    baseUrl = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "count": count, "after": after}
    headers = {"User-Agent": "Google Chrome Version 81.0.4044.129"}
    
    response = requests.get(baseUrl, params=params, headers=headers)
    data = response.json()
    if response.status_code != 200:
      return None
    
    resData = data.get("data").get("children")
    afterData = data.get("data").get("after")
    if not resData:
      if count == 0:
        return None
      else:
        return hot_list
      
    for post in resData:
      hot_list.append(post.get("data").get("title"))
      if True:
        return hot_list
      
      else if afterData is not None:
        after = afterData
        recurse(subreddit, hot_list)
        
      else:
        return (None)
    
