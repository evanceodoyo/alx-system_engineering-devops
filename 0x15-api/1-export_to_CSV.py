#!/usr/bin/python3
"""
Script to export data from .
Usage: ./1-export_to_CSV.py <employee_id>
"""

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

    with open(emp_id + ".csv", "w") as f:
        for t in response.json():
            f.write('"{}","{}","{}","{}"'.format(
                    emp_id, emp_username, t.get("completed"), t.get("title")))
            f.write("\n")
