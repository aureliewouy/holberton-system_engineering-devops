#!/usr/bin/python3
""" Recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles"""


import requests


def recurse(subreddit, hot_list=[], count=0):
    """
    Returns a list containing the titles of all hot articles
    """
    url_api = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-agent': 'My_user_agent'}
    response = requests.get(url_api, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return None
    else:
        try:
            data = response.json().get('data').get("children")[count]\
                                          .get("data").get("title")
            hot_list.append(data)
        except:
            return None
        recurse(subreddit, hot_list, count=count+1)
        return hot_list
