#!/usr/bin/python3
"""A module that Exports all employees data in the JSON format."""


from requests import get
import json
import requests
import sys


if __name__ == "__main__":
    user_url = f'https://jsonplaceholder.typicode.com/users/'
    user_response = requests.get(user_url)
    users = user_response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        todos_url = url + '/todos/'
        response = requests.get(todos_url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dictionary, f)
