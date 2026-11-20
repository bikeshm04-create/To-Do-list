def task():
    task = [] #emptylist
    print("----WELCOME TO THE TO-DO LIST APP----")

    total_task = int(input("Enter the number of tasks you want to do: "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i}: ")
        task.append(task_name)

    print(f"Today's tasks are:\n{task}")
    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation == 1:
            add = input("Enter task you want to add: ")
            task.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            update_val = input("Enter the task name you want to update: ")
            if update_val in task:
                up = input("Enter new task: ")
                ind = task.index(update_val) #1,2,...
                task[ind] = up
                print(f"Task {update_val} has been successfully updated to {up}...")

        elif operation == 3:
            del_val = input("Enter the task name you want to delete: ")
            if del_val in task:
                ind = task.index(del_val)
                del task[ind]
                print(f"Task {del_val} has been successfully deleted...")

        elif operation == 4:
            print(f"Total tasks are: {task}")

        elif operation == 5:
            print("Thank you for using the To-Do List App...")
            break

        else:
            print("Invalid input...Please try again...")

task()