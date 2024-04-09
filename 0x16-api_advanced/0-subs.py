#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    """
    user = {'User-agent': 'Google Chrome Version 123.0.6312.106'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user)
    data_res = response.json()

    try:
        return data_res.get('data').get('subsribers')
    except Exception:
        return 0


if __name__ == "__main__":
    subreddit = sys.argv[1]
    number_of_subsribers(subreddit)
