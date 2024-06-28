#!/usr/bin/python3
"""Script to fetch and display TODO list progress for a given employee ID."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display TODO list progress for the given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(f"{base_url}/users/{employee_id}/todos").json()

    completed = [t for t in todos if t['completed']]
    total = len(todos)
    done = len(completed)

    print(f"Employee {user['name']} is done with tasks({done}/{total}):")
    for task in completed:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
