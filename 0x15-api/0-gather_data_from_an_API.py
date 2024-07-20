#!/usr/bin/python3
"""API"""
import json
import requests
from sys import argv
if __name__ == "__main__":
    link = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    user_data = json.loads(requests.get(link).content.decode('utf8'))
    toddata = json.loads(requests.get(f"{link}/todos").content.decode('utf8'))
    total = len(toddata)
    done = 0
    for i in toddata:
        if i['completed']:
            done += 1
    print(f"Employee {user_data['name']} is done with tasks({done}/{total}):")
    for i in toddata:
        if i['completed']:
            print(f"\t {i['title']}")
