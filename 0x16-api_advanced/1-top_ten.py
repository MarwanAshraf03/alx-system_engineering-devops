#!/usr/bin/python3
"""
prints the number of subscribers to a subreddit
"""
import json
import requests


def top_ten(subreddit):
    """
    prints the number of subscribers to a subreddit
    """
    resp = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9")
    if resp.status_code != 200:
        print(None)
        return
    count = 1
    for i in json.loads(resp.text)['data']['children']:
        print(count, i['data']['title'])
        count += 1
