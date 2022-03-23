tasks = []

print("1. Add Task")
print("2. Update Task")
user_choice = input("Enter Your Choice: ")
if user_choice == "1":
    should_continue = True
    while should_continue:
        task = input("Enter the task you want to add: ")
        tasks.append(task + "\n")
        with open("data.txt", "w") as file:
            file.writelines(tasks)
        print("Task added")
        with open("data.txt", "r") as file:
            content = file.readlines()
            # Write Code logic here
            for i in range(len(content)):
                print(f"{i + 1}. {content[i]}")

        continue_adding = input("Do you want to continue: ")
        if continue_adding == "y":
            should_continue = True
        else:
            print("Thanks for using TaskBean!")
            should_continue = False
else:
    with open("data.txt", "r") as file:
        content = file.readlines()
        should_continue_1 = True
        while should_continue_1:
            if len(content) == 0:
                empty_list_choice = input("No Tasks Found, Do you want to add a new task?:").lower()

                if empty_list_choice == "y":
                    should_continue_2 = True
                    while should_continue_2:
                        new_task = input("Enter the task you want to add: ")
                        tasks.append(new_task + "\n")
                        with open("data.txt", "w") as file:
                            file.writelines(tasks)
                        print("Task added")
                        with open("data.txt", "r") as file:
                            content = file.readlines()
                            # Write Code logic here
                            for i in range(len(content)):
                                print(f"{i + 1}. {content[i]}")
                        continue_adding = input("Do you want to continue: ")
                        if continue_adding == "y":
                            should_continue_2 = True
                        else:
                            print("Thanks for using TaskBean!")
                            should_continue_2 = False
                            should_continue_1 = False
            else:
                update_list_choice = input("Do you want to update any tasks?:").lower()
                if update_list_choice == "y":
                    with open("data.txt", "r+") as new_file:
                        lines = new_file.readlines()
                        for i in range(len(lines)):
                            print(f"{i + 1}. {lines[i]}")
                    chosen_task_no = int(input("Enter the task you want to update:"))
                    chosen_task = lines[chosen_task_no - 1]
                    print(f"Chosen Task is {chosen_task}")
                    task_completed = input("Do you want to mark this task completed?:").lower()
                    if task_completed == "y" and lines:
                        with open("data.txt", "r+") as new_file:
                            lines = new_file.readlines()
                        with open("data.txt", "w") as new_file:
                            for line in lines:
                                if line != chosen_task:
                                    new_file.write(line)

                        print("This Task has been successfully completed.")
                        print("Below are the remaining tasks")
                        with open("data.txt", "r+") as new_file:
                            lines = new_file.readlines()
                            for i in range(len(lines)):
                                print(f"{i + 1}. {lines[i]}")
                    elif update_list_choice == "n":
                        should_continue_2 = False
                    else:
                        print("No Tasks Found, Add new Tasks.")
                else:
                    should_continue_1 = False
