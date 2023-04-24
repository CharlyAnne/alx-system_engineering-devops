#!/usr/bin/python3
"""Script extends to export data in JSON format"""

import sys
import requests
import json


if __name__ == '__main__':
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    employeeId = sys.argv[1]
    url = baseUrl + "/" + employeeId

    # Get employee name
    response = requests.get(url)
    username = response.json().get('username')

    # Get data on the ToDo of the employee
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    # records all tasks owned by an employee
    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
        
    # exports in JSON format
    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(dictionary, filename)
