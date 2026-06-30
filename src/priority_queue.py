import heapq

def create_priority_queue(tasks):

    heap = []

    for task in tasks:

        heapq.heappush(

            heap,

            (

                -task.priority,

                task.deadline,

                task

            )

        )

    return heap