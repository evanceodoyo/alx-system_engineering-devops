#!/usr/bin/python3
"""
Script to export data in JSON format.
Usage: ./3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    employees = requests.get(url).json()

    emp_data = {}
    for emp in employees:
        emp_id = str(emp.get('id'))
        emp_data[emp_id] = []

        emp_tasks = requests.get(url + emp_id + "/todos").json()
        for task in emp_tasks:
            task_data = {}
            task_data['username'] = emp.get('username')
            task_data['task'] = task.get('title')
            task_data['completed'] = task.get('completed')
            emp_data[emp_id].append(task_data)

    with open("todo_all_employees.json", "w") as f:
        json.dump(emp_data, f)
