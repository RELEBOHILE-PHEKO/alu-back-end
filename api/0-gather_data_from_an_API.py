#!/usr/bin/python3
"""
Script to fetch and display TODO list progress for a given employee ID
using a REST API.
"""

import sys
import requests

def get_employee_todo_progress(employee_id):
    """
    Fetch and display TODO list progress for the given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data['name']
    
    # Fetch TODO list
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])
    
    # Display progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    
    # Display completed tasks
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)
