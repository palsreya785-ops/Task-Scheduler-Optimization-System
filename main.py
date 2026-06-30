from src.load_tasks import load_tasks
from src.sort_tasks import sort_tasks
from src.priority_queue import create_priority_queue
from src.scheduler import schedule_tasks
from src.report import generate_report
from src.menu import display_menu
from src.add_task import add_task

while True:

    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        tasks = load_tasks("data/tasks.csv")

        print("\nCurrent Tasks\n")

        for task in tasks:
            print(task)

    elif choice == "2":

        tasks = load_tasks("data/tasks.csv")

        tasks = sort_tasks(tasks)

        heap = create_priority_queue(tasks)

        completed, missed, total_profit, timeline, total_time = schedule_tasks(heap)

        print("\n=========== SCHEDULE ===========")

        print("{:<20}{:<8}{:<8}{:<10}{:<10}".format(
            "Task",
            "Start",
            "End",
            "Deadline",
            "Status"
        ))

        print("-"*60)

        for t in timeline:

            print("{:<20}{:<8}{:<8}{:<10}{:<10}".format(
                t["task"],
                t["start"],
                t["end"],
                t["deadline"],
                t["status"]
            ))

        print("\nCompleted:", len(completed))
        print("Missed:", len(missed))
        print("Profit:", total_profit)

        generate_report(completed, missed, total_profit)

    elif choice == "3":

        add_task()

    elif choice == "4":

        print("\nThank you for using Task Scheduler!")

        break

    else:

        print("\nInvalid Choice")