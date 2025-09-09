# todo.py

tasks = []   # This is to empty task to store task

while True:   # 2 write all the command from 1 to 4
    print("\n--- TO-DO LIST ---")   # 3
    print("1. Add Task")           # 4
    print("2. View Tasks")         # 5
    print("3. Mark Task as Done") 
    print ("3.2. Review the Task") # 6
    print("4. Exit")               # 7

    choice = input("Enter choice (1-4): ")   # 8 give the choice to put the number wish to see. "Choice" work as multiple select

    if choice == "1":    # 9 "If" means either that or else another command.
        task = input("Enter new task: ")  # 10 "input" means the message to show.
        tasks.append(task)                # 11 "tasks.append(tasks)" is to store the new input in the empty task file above.
        print(f"Task added: {task}")      # 12 "f is the python string that saying to tell us know what added.

    elif choice == "2":   # 13 "elif" there is more than one if and diffent types of command.
        print("\nYour Tasks:")   # 14
        if not tasks:   # 15
            print("No tasks yet.")   # 16
        else:   # 17
            for i, t in enumerate(tasks, start=1):   # 18
                print(f"{i}. {t}") # enumerate means the loop of the f string like it gonna tell in order.i is the index number and t is the task.                 # 19

    elif choice == "3":   # 20
        print("\nWhich task number did you finish?")   # 21
        for i, t in enumerate(tasks, start=1):         # 22
            print(f"{i}. {t}")                         # 23
        num = int(input("Enter task number: "))        # 24
        if 1 <= num <= len(tasks):                     # 25
            finished = tasks.pop(num - 1) #pop(index)  removes an item from the list at that position.             # 26
            print(f"Task completed: {finished}")       # 27
        else:                                          # 28
            print("Invalid number.")                   # 29
    elif choice == "3.2":  
              print ("Have to learn more Haris!")
              
    elif choice == "4":   # 30
        print("Goodbye!")   # 31
        break               # 32

    else:   # 33
        print("Invalid choice. Try again.")   # 34
