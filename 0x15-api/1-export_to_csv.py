#!/usr/bin/python3
"""Script exports data in the CSV format"""

import sys
from sys import argv
import requests


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    # employee name
    response = requests.get(url)
    username = response.json().get('username')

    # TODO info
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    # CSV format
    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                        .format(employeeId, username, task.get('completed'),
                                task.get('title')))

