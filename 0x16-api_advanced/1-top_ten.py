#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests
from sys import argv


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    """
    user = {'User-agent': 'Custom'}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=user)
    data_res = response.json()

    try:
        for item in data_res.get('data').get('children'):
            print(item.get('data').get('title'))
    except Exception:
        print('None')


if __name__ == "__main__":
    top_ten(argv[1])
