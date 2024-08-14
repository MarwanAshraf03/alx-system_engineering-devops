#!/usr/bin/python3
"""
prints the number of subscribers to a subreddit
"""
import json
import requests


def recurse(subreddit, hot_list=[]):
    """
    prints the number of subscribers to a subreddit
    """
    subreddit = subreddit.split('-')
    p = {'limit': 100}
    if len(subreddit) > 1:
        p['after'] = subreddit[1]
    resp = requests.get(
        f"https://www.reddit.com/r/{subreddit[0]}/hot.json",
        params=p)
    if resp.status_code != 200:
        return (None)
    for i in json.loads(resp.text)['data']['children']:
        hot_list.append(i['data']['title'])
    after = json.loads(resp.text)['data']['after']
    if after:
        recurse(f"{subreddit[0]}-{after}", hot_list)
    return (hot_list)
