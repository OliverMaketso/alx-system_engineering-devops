#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees
Export data in the CSV format."""


from requests import get
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

    with open('{}.csv'.format(user_ID), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_ID, user_name, task.get('completed'),
                               task.get('title')))
