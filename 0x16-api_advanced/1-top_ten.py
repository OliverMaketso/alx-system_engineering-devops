#!/usr/bin/python3
"""module to querry a Reddit API."""
from requests import get


def top_ten(subreddit):
    """queries the Reddit API
    returns the top 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    results = get(url, headers, allow_redirects=False)
    if results.status_code == 200:
        for post in results.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
