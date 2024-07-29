#!/usr/bin/python3
"""Module that uses REST API, for a given employee ID, returns information
about his/her TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    user_ID = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_ID}'
    user_response = requests.get(user_url)
    user_name = user_response.json().get('name')

    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_ID}'
    todos_response = requests.get(todos_url)
    tasks = todos_response.json()
    total_tasks_done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            total_tasks_done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, total_tasks_done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
