#!/usr/bin/python3
"""
prints the number of subscribers to a subreddit
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    prints the number of subscribers to a subreddit
    """
    resp = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
    if resp.status_code != 200:
        return (0)
    return (json.loads(resp.text)['data']['subscribers'])
