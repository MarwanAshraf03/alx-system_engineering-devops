#!/usr/bin/python3
"""
prints the number of subscribers to a subreddit
"""
import json
import requests


def count_words(subreddit, word_list, word_dict={}):
    """
    prints the number of subscribers to a subreddit
    """
    if (word_dict == {}):
        for i in word_list:
            word_dict[i.lower()] = 0
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
        for j in i['data']['title'].lower().split():
            if j in word_dict.keys():
                word_dict[j] += 1

    after = json.loads(resp.text)['data']['after']
    if after:
        count_words(f"{subreddit[0]}-{after}", word_list, word_dict)
    else:
        # print(word_dict)
        word_dict = {k: v for k, v in sorted(word_dict.items(),
                                             key=lambda item: item[1],
                                             reverse=True)}
        for i in word_dict.keys():
            if word_dict[i] != 0:
                print(f"{i}: {word_dict[i]}")
