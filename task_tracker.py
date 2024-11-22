import os
import json
import argparse
from datetime import datetime

# Filepath for the tasks JSON file
TASKS_FILE = "tasks.json"

# Function to initialize the tasks.json file if it doesn't exist or is empty
def initialize_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as file:
            json.dump([], file)  # Initialize as an empty list
        print(f"{TASKS_FILE} created successfully!")
    else:
        # Ensure file has valid JSON content (an empty list if empty)
        with open(TASKS_FILE, 'r+') as file:
            content = file.read().strip()
            if not content:  # File is empty
                file.seek(0)
                json.dump([], file)
                print(f"{TASKS_FILE} was empty and has been initialized.")

# Function to load tasks from the JSON file
def load_tasks():
    with open(TASKS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []  # Return an empty list if JSON is invalid

# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to generate a unique ID for a task
def generate_task_id(tasks):
    return max([task['id'] for task in tasks], default=0) + 1

# Function to add a new task
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": generate_task_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {new_task}")

# Function to list all tasks or filter by status
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']} | Created At: {task['createdAt']} | Updated At: {task['updatedAt']}")

# Function to update a task's description or status
def update_task(task_id, description=None, status=None):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task:
        if description:
            task['description'] = description
        if status:
            if status in ['todo', 'in-progress', 'done']:
                task['status'] = status
            else:
                print("Invalid status. Use 'todo', 'in-progress', or 'done'.")
                return
        task['updatedAt'] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task updated: {task}")
    else:
        print(f"Task with ID {task_id} not found.")

# Function to delete a task
def delete_task(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task:
        tasks = [t for t in tasks if t['id'] != task_id]
        save_tasks(tasks)
        print(f"Task with ID {task_id} deleted.")
    else:
        print(f"Task with ID {task_id} not found.")

# Main function to handle CLI commands
def main():
    initialize_file()
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Subcommand for adding a task
    add_parser = subparsers.add_parser('add', help="Add a new task")
    add_parser.add_argument('--description', help="Description of the task to add", required=True)

    # Subcommand for listing tasks
    list_parser = subparsers.add_parser('list', help="List all tasks")
    list_parser.add_argument('--status', choices=['todo', 'in-progress', 'done'], help="Filter tasks by status")

    # Subcommand for updating a task
    update_parser = subparsers.add_parser('update', help="Update an existing task")
    update_parser.add_argument('id', type=int, help="ID of the task to update")
    update_parser.add_argument('--description', help="New description for the task")
    update_parser.add_argument('--status', choices=['todo', 'in-progress', 'done'], help="New status for the task")

    # Subcommand for deleting a task
    delete_parser = subparsers.add_parser('delete', help="Delete a task")
    delete_parser.add_argument('id', type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if args.command == 'add' and args.description:
        add_task(args.description)
    elif args.command == 'list':
        list_tasks(args.status)
    elif args.command == 'update':
        update_task(args.id, args.description, args.status)
    elif args.command == 'delete':
        delete_task(args.id)
    else:
        print("Invalid command or missing arguments. Use --help for usage details.")

if __name__ == "__main__":
    main()
