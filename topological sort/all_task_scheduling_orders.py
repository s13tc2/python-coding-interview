# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
# Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
# Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

from collections import deque

# O(v!*e) time | O(v!*e) space
def print_orders(tasks, prerequisites):
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
    print_all_topological_sort(sources, inDegree, graph, sortedOrder)


def print_all_topological_sort(sources, inDegree, graph, sortedOrder):
    if sources:
        for vertex in sources:
            sortedOrder.append(vertex)
            sourcesForNextCall = deque(sources)
            sourcesForNextCall.remove(vertex)

            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sourcesForNextCall.append(child)

            print_all_topological_sort(sourcesForNextCall, inDegree, graph, sortedOrder)

            sortedOrder.remove(vertex)
            for child in graph[vertex]:
                inDegree[child] += 1
    if len(sortedOrder) == len(inDegree):
        print(sortedOrder)


if __name__ == "__main__":
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
