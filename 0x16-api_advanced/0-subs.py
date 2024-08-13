#!/usr/bin/python3
import json
import requests
"""
0-main
"""


def number_of_subscribers(subreddit):
    resp = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
    if resp.status_code != 200:
        return (0)
    return (json.loads(resp.text)['data']['subscribers'])
