#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees
Export data in the JSON format."""


from requests import get
import json
import requests
import sys


if __name__ == "__main__":
    user_ID = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_ID}'
    user_response = requests.get(user_url)
    user_name = user_response.json().get('username')

    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_ID}'
    todos_response = requests.get(todos_url)
    tasks = todos_response.json()

    dictionary = {user_ID: []}

    for task in tasks:
        dictionary[user_ID].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_name
        })

    with open('{}.json'.format(user_ID), 'w') as f:
        json.dump(dictionary, f)
