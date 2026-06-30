import csv

def add_task():

    print("\nEnter Task Details\n")

    name = input("Task Name: ")

    priority = input("Priority (1-5): ")

    deadline = input("Deadline: ")

    execution = input("Execution Time: ")

    profit = input("Profit: ")

    with open("data/tasks.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            name,
            priority,
            deadline,
            execution,
            profit
        ])

    print("\nTask Added Successfully!")