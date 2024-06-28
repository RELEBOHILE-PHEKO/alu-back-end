#!/usr/bin/python3
"""
Script to fetch TODO list progress for a given employee ID
and export the data in JSON format.
"""
import json
import requests
import sys


def export_to_json(employee_id):
    """
    Fetch TODO list for the given employee ID and export to JSON.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    username = user['username']

    # Fetch TODO list
    todos = requests.get(f"{base_url}/users/{employee_id}/todos").json()

    # Prepare JSON data
    json_data = {
        str(employee_id): [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
            }
            for todo in todos
        ]
    }

    # Prepare JSON file name
    json_filename = f"{employee_id}.json"

    # Write data to JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
