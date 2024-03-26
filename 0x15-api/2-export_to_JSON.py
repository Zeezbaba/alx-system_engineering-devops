#!/usr/bin/python3
"""
script to export data in the CSV format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com"
    userUrl = f"{baseUrl}/users"
    url = userUrl + "/" + employeeId

    """Fetching user data"""
    userResponse = requests.get(url)
    userName = userResponse.json().get('username')

    """Fetching todo list"""
    todoUrl = url + "/todos"
    todoResponse = requests.get(todoUrl)
    todoTask = todoResponse.json()

    dict_data = {employeeId: []}
    for task in todoTask:
        dict_data[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": userName})
    with open('{}.json'.format(employeeId), 'w') as f:
        json.dump(dict_data, f)
