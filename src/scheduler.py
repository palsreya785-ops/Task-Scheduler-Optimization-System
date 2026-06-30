import heapq

def schedule_tasks(heap):

    current_time = 0

    completed = []
    missed = []

    total_profit = 0

    timeline = []

    while heap:

        _, _, task = heapq.heappop(heap)

        start_time = current_time
        end_time = start_time + task.execution

        current_time = end_time

        if end_time <= task.deadline:
            status = "On Time"
            completed.append(task)
            total_profit += task.profit
        else:
            status = "Late"
            missed.append(task)

        timeline.append({
            "task": task.name,
            "start": start_time,
            "end": end_time,
            "deadline": task.deadline,
            "status": status
        })

    return completed, missed, total_profit, timeline, current_time