# Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

# Given a directed graph, find the topological ordering of its vertices.

from collections import deque

# O(V+E) time | O(V+E) space
def topological_sort(vertices, edges):
    inDegree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        parent, child = edge[0], edge[1]
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

    if len(sortedOrder) != vertices:
        return []
    return sortedOrder


if __name__ == "__main__":
    print(
        "Topological sort: "
        + str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
    )
    print(
        "Topological sort: "
        + str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
    )
    print(
        "Topological sort: "
        + str(
            topological_sort(
                7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
            )
        )
    )
