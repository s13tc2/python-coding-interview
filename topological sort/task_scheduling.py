# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
# Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
# Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

from collections import deque

# O(v+e) time | O(v+e) space
def is_scheduling_possible(tasks, prerequisites):
    inDegree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for pre in prerequisites:
        parent, child = pre[0], pre[1]
        inDegree[child] += 1
        graph[parent].append(child)

    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    sortedOrder = []
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    return len(sortedOrder) == tasks


if __name__ == "__main__":
    print("Is scheduling possible: " + str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print(
        "Is scheduling possible: "
        + str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]]))
    )
    print(
        "Is scheduling possible: "
        + str(
            is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
        )
    )
