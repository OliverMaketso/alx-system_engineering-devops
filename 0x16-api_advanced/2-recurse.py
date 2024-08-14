#!/usr/bin/python3
"""module to querry a Reddit API."""
from requests import get


def recurse(subreddit, hot_list=[], n=0, after=None):
    """queries the Reddit API
    Args:
        subreddit (str): subreddit.
        hot_list (list, optional): list of titles

    return:
        list containing the titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    results = get(url, headers, allow_redirects=False)
    if results.status_code == 200:
        results = results.json()
        for post in results['data']['children']:
            hot_list.append(post['data']['title'])
        if results['data']['after']:
            recurse(subreddit, hot_list)
            return hot_list
    else:
        return None
