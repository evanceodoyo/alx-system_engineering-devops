#!/usr/bin/python3
"""
Script to export data in JSON format.
Usage: ./2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Please provide an employee ID")

    emp_id = sys.argv[1]
    if not emp_id.isdigit():
        sys.exit("Employee ID must be an integer.")

    response = requests.get("https://jsonplaceholder.typicode.com/todos",
                            params={"userId": emp_id})
    emp_username = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(emp_id)).json().get('username')

    tasks = []
    for t in response.json():
        tasks.append({"task": t.get('title'),
                      "completed": t.get('completed'),
                      "username": emp_username})

    with open(emp_id + ".json", "w") as f:
        json.dump({emp_id: tasks}, f)
