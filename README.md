# Task Tracker CLI Application

A simple command-line interface (CLI) task tracker built in Python. This application allows you to manage tasks through various commands such as adding, updating, deleting, and listing tasks with different statuses.

## Features

- **Add a task**: Add a new task with a description.
- **Update a task**: Update the description or status of an existing task.
- **Delete a task**: Delete a task by its ID.
- **List tasks**: View all tasks or filter tasks by their status (todo, in-progress, done).
- **Mark tasks with a status**: Set the status of tasks to `todo`, `in-progress`, or `done`.

## Requirements

- Python 3.x (The code has been tested with Python 3.10)

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project folder.

```bash
cd Task_Project
```

## Usage

### Add a Task

To add a new task with a description:

```bash
python task_tracker.py add --description "Your Task Description Here"
```

### List Tasks

To list all tasks:

```bash
python task_tracker.py list
```

To list tasks filtered by status (e.g., `todo`, `in-progress`, or `done`):

```bash
python task_tracker.py list --status todo
```

### Update a Task

To update the description or status of an existing task:

```bash
python task_tracker.py update <task_id> --description "Updated Description"
python task_tracker.py update <task_id> --status done
```

### Delete a Task

To delete a task by its ID:

```bash
python task_tracker.py delete <task_id>
```

## File Structure

- **task_tracker.py**: Main Python script that implements the task tracker functionality.
- **tasks.json**: JSON file that stores task data. If the file doesn't exist, it will be created automatically.
- **README.md**: Documentation for using the Task Tracker CLI Application.

## Notes

- If `tasks.json` does not exist, it will be created automatically when adding a task.
- Task IDs are unique and are automatically assigned when a task is added.
- The task's status can be set to `todo`, `in-progress`, or `done`.

## License

This project is open-source and available under the MIT License.
```

### Key Changes:
- **Usage** section now has proper headings and consistent formatting with triple backticks for code blocks.
- Added missing closing ```bash for the command sections.

Now, you can copy this and paste it into your `README.md` file.
