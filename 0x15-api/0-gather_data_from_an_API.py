#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com"
    userUrl = f"{baseUrl}/users"
    url = userUrl + "/" + employeeId

    """Fetching user data"""
    userResponse = requests.get(url)
    employeeName = userResponse.json().get('name')

    """Fetching todo list"""
    todoUrl = url + "/todos"
    todoResponse = requests.get(todoUrl)
    todoTask = todoResponse.json()
    totalTask = 0
    doneTask = []

    for task in todoTask:
        if task.get('completed'):
            doneTask.append(task)
            totalTask += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, totalTask, len(todoTask)))

    for task in doneTask:
        print("\t {}".format(task.get('title')))
