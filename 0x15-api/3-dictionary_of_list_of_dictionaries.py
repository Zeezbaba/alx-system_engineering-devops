#!/usr/bin/python3
"""extend Python script to export data in the JSON format."""

import json
import requests
import sys


if __name__ == '__main__':
    baseUrl = "https://jsonplaceholder.typicode.com"
    userUrl = f"{baseUrl}/users"

    """Fetching users rrsponse"""
    userResponse = requests.get(userUrl)
    userData = userResponse.json()

    dict_data = {}
    for user in userData:
        userId = user.get('id')
        userName = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
        todoUrl = url + '/todos/'
        todoResponse = requests.get(todoUrl)
        todoTask = todoResponse.json()
        dict_data[userId] = []
        for task in todoTask:
            dict_data[userId].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": userName})
    with open('todo_all_employees.json', 'w') as jsonFile:
        json.dump(dict_data, jsonFile)
