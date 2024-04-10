#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    returns a list containing the titles of all hot
    articles for a given subreddit
    """
    global after
    user = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, params=parameters, headers=user,
                           allow_redirects=False)

    if response.status_code == 200:
        data_res = response.json().get("data").get("after")
        if data_res is not None:
            after = data_res
            recurse(subreddit, hot_list)
        all_titles = response.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
