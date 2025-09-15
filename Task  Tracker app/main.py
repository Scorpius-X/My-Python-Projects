# Add, Update, and Delete tasks

# Mark a task as in progress or done

# List all tasks

# List all tasks that are done

# List all tasks that are not done

# List all tasks that are in progress



#initiate task list
tasks = []

description = {}

#auxiliary function
def display_tasks(all_tasks):
    print("\nYour Tasks: ")

    if len(all_tasks) <= 0:
        print("No Task! left")
    else:
        for index, task in enumerate(all_tasks):
            print(f"{index+1}: {task}")



def new_operation(all_tasks):
    operation = input("\ninput 'A' to add a new task, input 'E' to edit a task," \
    "\ninput 'R' to remove a task, input 'D' to display task," \
    "\ninput 'D' to display all task, input 'F' to Quit: ").upper()
    
    if operation == 'A':
        add_task(all_tasks)
    elif operation == "B":
        pass
    elif operation == "R":
        remove_task(all_tasks)
    elif operation == "F":
        return
    else:
        new_operation(all_tasks)

def valid_task_number(all_tasks,operation):
    task_number = input(f"enter the number of the task you want to {operation}: ")

    valid = False

    while not valid:
        try:
            number = int(task_number)
            valid = True
        except:
            task_number = input("please provide a valid task number: ")
        
    if not(0 < number <= len(all_tasks)):
        print("Task not found")
        valid_task_number(all_tasks,operation)
    else:
        return number

# def add_description(description):



def edit_task(all_tasks):
    task_number = valid_task_number(all_tasks, "edit")

    new_task = input("Enter the edited task: ")

    all_tasks[(task_number)-1] = new_task

    print(f"\nItem number {task_number} has been edited!")

    new_operation(all_tasks)

def remove_task(all_tasks):
    task_number = valid_task_number(all_tasks, "remove")
    
    all_tasks.remove(all_tasks[(task_number)-1])

    print(f"\nItem number {task_number} has been removed!")

    new_operation(all_tasks)

def add_task(all_tasks):
    new_task = input("Add a Task: ")
    all_tasks.append(new_task)

    print("Task added Successfully!")

    new_operation(all_tasks)

# start app
add_task(tasks)