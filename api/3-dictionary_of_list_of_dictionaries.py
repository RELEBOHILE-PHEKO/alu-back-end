#!/usr/bin/python3
"""
Script to fetch TODO list progress for all employees
and export the data in JSON format.
"""
import json
import requests


def export_all_to_json():
    """
    Fetch TODO list for all employees and export to JSON.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users = requests.get(f"{base_url}/users").json()

    # Prepare JSON data
    all_tasks = {}

    for user in users:
        user_id = str(user['id'])
        username = user['username']

        # Fetch TODO list for the user
        todos = requests.get(f"{base_url}/users/{user_id}/todos").json()

        # Add tasks to the user's list
        all_tasks[user_id] = [
            {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in todos
        ]

    # Prepare JSON file name
    json_filename = "todo_all_employees.json"

    # Write data to JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(all_tasks, json_file)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    export_all_to_json()
