import json

def load_task():
    try:
        with open('task.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(task):
    with open('task.txt', 'w') as file:
        return json.dump(task, file)
    

def view_tasks(task):
    print("\n")
    print("*" * 100)
    for index, tasks in enumerate(task, start=1):
        print(f"{index}. {tasks['name']}") 
    print("\n")
    print("*" * 100)


def add_task(task): 
    name = input("Enter the task: ")
    task.append({'name': name})
    save_data(task) 


def update_task(task):
    view_tasks(task)

    index = int(input("Enter the task number to update: "))

    if 1<= index <= len(task):
        name = input("Enter the new task: ")
        task[index-1] = {'name': name} 
        save_data(task)
    
    else:
        print("Invalid index !!!")

def delete_task(task):
    view_tasks(task)

    index = int(input("Enter the task number to be deleted: "))

    if 1<= index <=len(task):
        del task[index-1]
        save_data(task)
    
    else:
        print("Invalid Index !!!")


def main():
    
    task = load_task()

    while True:
        print("------To-Do List------")
        print("\n")
        print("1. View all tasks")
        print("2. Add new task")
        print("3. Update a task")
        print("4. Delete a tasks")
        print("5. Exit the app")
        print("\n")

        choice = input("Enter the choice: ")
        match choice:
            case '1':
                view_tasks(task)

            case '2':
                add_task(task)

            case '3':
                update_task(task)

            case '4':
                delete_task(task)

            case '5':
                break

            case _:
                print("Invalid Input")

if __name__ == "__main__":
    main()