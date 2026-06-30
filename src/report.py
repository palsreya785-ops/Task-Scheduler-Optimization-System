import csv

def generate_report(completed, missed, total_profit):

    with open("outputs/report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Completed Tasks"])

        writer.writerow(
            ["Task", "Priority", "Deadline", "Execution", "Profit"]
        )

        for task in completed:
            writer.writerow([
                task.name,
                task.priority,
                task.deadline,
                task.execution,
                task.profit
            ])

        writer.writerow([])

        writer.writerow(["Missed Tasks"])

        writer.writerow(
            ["Task", "Priority", "Deadline", "Execution", "Profit"]
        )

        for task in missed:
            writer.writerow([
                task.name,
                task.priority,
                task.deadline,
                task.execution,
                task.profit
            ])

        writer.writerow([])

        writer.writerow(["Total Profit", total_profit])