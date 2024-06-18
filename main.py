import json

tasks = []

def add_task(task):
    user_input = task
    tasks.append(user_input)
    print(tasks)
    return

def remove_task(index):
    if index < len(tasks):
        del tasks[index]
        print(tasks)
    else:
        print("Ungültige Index")

def list_tasks():
    print(tasks)
    return

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

while True:
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List all tasks")
    print("4. Exit")

    choice = int(input("What do you want to do? "))
    if choice == 1:
        add_task(input("Your Task: "))
    elif choice == 2:
        remove_task(int(input("Delete a Task: ")))
    elif choice == 3:
        list_tasks()
    elif choice == 4:
        break
    else:
        print("Ungültige Nummer")