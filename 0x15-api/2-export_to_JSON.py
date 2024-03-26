#!/usr/bin/python3
"""API"""
import json
import requests
from sys import argv
if __name__ == "__main__":
    link = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    d = json.loads(requests.get(f"{link}/todos").content.decode('utf8'))
    u = json.loads(requests.get(f"{link}").content.decode('utf8'))
    id = argv[1]
    name = u['username']
    dictlist = []
    for i in d:
        dict = {}
        dict['task'] = i['title']
        dict['completed'] = i['completed']
        dict['username'] = name
        dictlist.append(dict)
    j = {
        str(id): dictlist
    }
    with open(f'{argv[1]}.json', 'w') as f:
        f.write(json.dumps(j))
