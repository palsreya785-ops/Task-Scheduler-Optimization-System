class Task:

    def __init__(self, name, priority, deadline, execution, profit):

        self.name = name
        self.priority = int(priority)
        self.deadline = int(deadline)
        self.execution = int(execution)
        self.profit = int(profit)

    def __str__(self):

        return (
            f"{self.name} | "
            f"Priority:{self.priority} | "
            f"Deadline:{self.deadline} | "
            f"Execution:{self.execution} | "
            f"Profit:{self.profit}"
        )