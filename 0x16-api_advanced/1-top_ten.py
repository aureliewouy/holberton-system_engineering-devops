#!/usr/bin/python3
""" Queries the Reddit API and prints the titles of the first
 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """
    Returns 10 hot posts
    """
    url_api = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'user_agent'}
    response = requests.get(url_api, headers=headers)
    if response.status_code == 404:
        print('None')
    else:
        for posts in response.json().get('data').get('children'):
            print(posts.get('data').get('title'))
