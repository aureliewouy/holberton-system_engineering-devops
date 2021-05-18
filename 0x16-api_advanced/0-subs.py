#!/usr/bin/python3
""" Function that queries the Reddit API
and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers of 0
    """
    url_api = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': 'user_agent'}
    response = requests.get(url_api, headers=headers)
    if response.status_code == 404:
        return 0
    return response.json().get('data').get('subscribers')
