import csv
from src.task import Task

def load_tasks(filename):

    tasks = []

    with open(filename, newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if (
                row["Task"] and
                row["Priority"] and
                row["Deadline"] and
                row["ExecutionTime"] and
                row["Profit"]
            ):

                task = Task(
                    row["Task"],
                    row["Priority"],
                    row["Deadline"],
                    row["ExecutionTime"],
                    row["Profit"]
                )

                tasks.append(task)

    return tasks