# -------------------------------------------------------------
#              SIMPLE TO-DO LIST MANAGER (EXPANDED)
# -------------------------------------------------------------
#
#   This program allows the user to:
#       1. Add tasks
#       2. View tasks
#       3. Delete tasks
#       4. Mark tasks as completed
#       5. Exit the program
#
#   NOTE:
#   No new features have been added. The code has simply been
#   expanded with comments, spacing, structure, and clarity
#   to increase the total line count to around 150–200 lines.
#
# -------------------------------------------------------------


# -------------------------------------------------------------
# GLOBAL TASK LIST
# -------------------------------------------------------------

tasks = []     # This list holds all the tasks added by the user



# -------------------------------------------------------------
# FUNCTION: add_task
# DESCRIPTION:
#    Prompts the user for a new task, strips whitespace, and
#    appends it to the global list of tasks.
# -------------------------------------------------------------

def add_task():
    """
    Adds a new task entered by the user to the task list.
    """

    # Prompt user for input
    task = input("Enter a new task: ").strip()

    # Add task to the global list
    tasks.append(task)

    # Confirmation message
    print(f"Task '{task}' added successfully!\n")



# -------------------------------------------------------------
# FUNCTION: view_tasks
# DESCRIPTION:
#    Prints the list of tasks in a clean numbered format. If
#    no tasks are available, displays a message.
# -------------------------------------------------------------

def view_tasks():
    """
    Displays all the tasks in the list in a numbered format.
    """

    # If no tasks exist, notify the user
    if not tasks:
        print("No tasks added yet.\n")
        return

    # Header for task display section
    print("\n---------- YOUR TASKS ----------")

    # Loop through all tasks using enumerate
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    # Footer for task display section
    print("--------------------------------\n")



# -------------------------------------------------------------
# FUNCTION: delete_task
# DESCRIPTION:
#    Displays tasks, asks the user which one should be removed,
#    and deletes it from the list.
# -------------------------------------------------------------

def delete_task():
    """
    Deletes a task from the list based on user selection.
    """

    # Show tasks before deletion
    view_tasks()

    # If there are still no tasks, exit
    if not tasks:
        return

    # Attempt to delete a valid task
    try:
        # Ask the user for task number
        number = int(input("Enter task number to delete: "))

        # Check if number is within valid range
        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            print(f"Task '{removed_task}' deleted successfully!\n")

        else:
            print("Invalid task number.\n")

    except ValueError:
        # Handle non-integer input
        print("Please enter a valid number.\n")



# -------------------------------------------------------------
# FUNCTION: mark_task_completed
# DESCRIPTION:
#    Displays tasks and asks the user which task should be
#    marked as completed. Appends “(Completed)” to that task.
# -------------------------------------------------------------

def mark_task_completed():
    """
    Marks a selected task as completed.
    """

    # Show tasks before marking completion
    view_tasks()

    # If there are no tasks, exit the function
    if not tasks:
        return

    try:
        # Ask for the task number
        number = int(input("Enter task number to mark completed: "))

        # Check if choice is valid
        if 1 <= number <= len(tasks):

            # Modify the selected task
            tasks[number - 1] = tasks[number - 1] + " (Completed)"

            print("Task marked as completed!\n")

        else:
            print("Invalid task number.\n")

    except ValueError:
        # Handle invalid (non-numeric) input
        print("Please enter a valid number.\n")



# -------------------------------------------------------------
# FUNCTION: show_menu
# DESCRIPTION:
#    Prints the main menu every time the loop executes.
# -------------------------------------------------------------

def show_menu():
    """
    Prints the list of menu options available to the user.
    """
    print("============== TO-DO LIST MENU ==============")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")
    print("=============================================")



# -------------------------------------------------------------
# FUNCTION: main
# DESCRIPTION:
#    Core loop of the program. Continuously displays options
#    and performs actions based on user input.
# -------------------------------------------------------------

def main():
    """
    Runs the main menu loop for the To-Do List application.
    """

    while True:

        # Display menu options
        show_menu()

        # Prompt user for menu choice
        choice = input("Enter your choice: ")

        # Evaluate user selection
        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            mark_task_completed()

        elif choice == "5":
            print("Exiting To-Do List...")
            break

        else:
            # Handle unexpected menu input
            print("Invalid choice. Try again.\n")



# -------------------------------------------------------------
# PROGRAM ENTRY POINT
# -------------------------------------------------------------

# Execute main only when script is run directly
main()

# -------------------------------------------------------------
#                   END OF PROGRAM
# -------------------------------------------------------------