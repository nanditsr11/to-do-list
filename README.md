# To-Do List Application

This is a simple command-line To-Do List application written in Python. The application allows users to view, add, update, and delete tasks. Tasks are saved to a file (`task.txt`) so that they persist between sessions.

## Features

- **View Tasks**: Display a list of all current tasks.
- **Add Task**: Add a new task to your To-Do list.
- **Update Task**: Modify an existing task.
- **Delete Task**: Remove a task from your list.
- **Persistent Storage**: Tasks are saved to a file so they can be accessed later.

## Prerequisites

- Python 3.x

## How to Run

1. **Clone the Repository**:  
   If you have not done so already, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-folder>

## File Structure
main.py: The main Python script containing the To-Do List application code.
task.txt: The file where tasks are stored. This file will be automatically created in the same directory as main.py if it does not exist.

## Notes
If the task.txt file does not exist, it will be created when you add your first task.
Tasks are stored in JSON format within the task.txt file.
Ensure that the task.txt file is in the same directory as the Python script when running the application.

## Example
Here's a quick example of what using the application might look like:

------To-Do List------

1. View all tasks
2. Add new task
3. Update a task
4. Delete a task
5. Exit the app

Enter the choice: 2
Enter the task: Buy groceries

Task added successfully!

------To-Do List------

1. View all tasks
2. Add new task
3. Update a task
4. Delete a task
5. Exit the app

Enter the choice: 1

****************************************************************************************************
1. Buy groceries
****************************************************************************************************

## License
This project is licensed under the MIT License - see the LICENSE file for details.
