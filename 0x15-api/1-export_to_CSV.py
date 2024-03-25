#!/usr/bin/python3
"""
script to export data in the CSV format.
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
    userName = userResponse.json().get('username')

    """Fetching todo list"""
    todoUrl = url + "/todos"
    todoResponse = requests.get(todoUrl)
    todoTask = todoResponse.json()

    with open('{}.csv'.format(employeeId), 'w') as csvfile:
        for task in todoTask:
            csvfile.write('"{}","{}","{}","{}"\n'
                          .format(employeeId, userName, task.get('completed'),
                                  task.get('title')))
