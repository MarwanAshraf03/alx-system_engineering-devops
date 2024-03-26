#!/usr/bin/python3
"""API"""
import json
import requests
from sys import argv
if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/users/"
    u = json.loads(requests.get(f"{link}").content.decode('utf8'))
    bdict = {}
    for i in u:
        li = []
        id = i['id']
        name = i['username']
        d = json.loads(requests.get(f"{link}/{id}"
                                    f"/todos").content.decode('utf8'))
        for j in d:
            sdict = {}
            sdict['username'] = name
            sdict['task'] = j['title']
            sdict['completed'] = j['completed']
            li.append(sdict)
        bdict[id] = li
    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(bdict))
