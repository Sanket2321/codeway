# Add a task to the tasks list
tasks=[]
def add_task():
    task = input("Enter the new task:")
    tasks.append(task)
    print("Task added successfully...")

# Display the list of tasks
def view_task():
    if len(tasks) == 0:
        print("No tasks")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f'{i + 1}. {task}')

# Delete a task from the tasks list
def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f'{i + 1}. {task}')
        choice = int(input("Enter the task number to delete:"))
        if 0 < choice <= len(tasks):
            del tasks[choice - 1]
            print('Task deleted successfully..')
        else:
            print('Invalid task number.')

# Main function to run the application
def main():
    while True:
        print("\n\n************TO-DO List Application*******************")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Thanks for using the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
