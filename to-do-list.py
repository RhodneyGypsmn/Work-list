#Simple To-Do-List
#Intialise an empty list to tasks
tasks = []
def show_menu():
    print("\nTo-Do-List Menu: ")
    print("1. Add a task ") 
    print("2. View all tasks ")
    print("3. Remove a task ")
    print("4. Exit ")
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")
def view_tasks():
    if not tasks:
        print("Your to-do-list is empty!")
    else:
        print("\nYour To-Do-List: ")
        for idx, task in enumerate(tasks, start=1):
               print(f"{idx}. {task}")
