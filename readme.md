# To-Do List Manager

A simple command-line to-do list application built with Python that helps you manage your daily tasks efficiently.

## Features

- **Add Tasks**: Create new tasks and add them to your list
- **View Tasks**: Display all current tasks with numbered indices
- **Delete Tasks**: Remove completed or unwanted tasks
- **Mark as Completed**: Track which tasks you've finished
- **User-Friendly Menu**: Easy-to-navigate interface

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository
2. Ensure Python 3 is installed on your system
3. No additional dependencies required

## Usage

Run the program using:

```bash
python todo_list.py
```

### Menu Options

1. **Add Task** - Enter a task description to add it to your list
2. **View Tasks** - See all your current tasks
3. **Delete Task** - Remove a task by its number
4. **Mark Task as Completed** - Append "(Completed)" to a finished task
5. **Exit** - Close the application

### Example Workflow

```
=== TO-DO LIST MENU ===
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Completed
5. Exit
Enter your choice: 1
Enter a new task: Buy groceries
Task 'Buy groceries' added successfully!
```

## Code Structure

- `tasks[]` - Global list storing all tasks
- `add_task()` - Handles adding new tasks
- `view_tasks()` - Displays all current tasks
- `delete_task()` - Removes tasks by index
- `mark_task_completed()` - Marks tasks as done
- `main()` - Main program loop with menu

## Limitations

- Tasks are stored in memory only (not persisted to disk)
- All data is lost when the program exits
- No task editing functionality
- Completed tasks remain in the list with "(Completed)" suffix

## Future Enhancements

- Save tasks to a file for persistence
- Edit existing tasks
- Set task priorities or due dates
- Filter tasks by status
- Export tasks to different formats

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!