#!/usr/bin/python3
"""module to querry a Reddit API."""
from requests import get


def number_of_subscribers(subreddit):
    """queries the Reddit API and
    returns the number of subscribers
    for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    results = get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if results.status_code == 200:
        return results.json()['data']['subscribers']
    return 0
