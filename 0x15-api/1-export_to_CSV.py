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
    with open(f'{argv[1]}.csv', 'w') as f:
        for i in d:
            f.write(f'"{id}","{name}","{i["completed"]}","{i["title"]}"\n')
