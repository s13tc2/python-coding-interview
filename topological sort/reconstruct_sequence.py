# Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.

# Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the array are subsequences of it.

from collections import deque

# O(v+n) time | O(v+n) space
def can_construct(originalSeq, sequences):
    sortedOrder = []
    if len(originalSeq) <= 0:
        return False

    inDegree = {}  
    graph = {} 
    for sequence in sequences:
        for num in sequence:
            inDegree[num] = 0
            graph[num] = []

    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i - 1], sequence[i]
            graph[parent].append(child)
            inDegree[child] += 1

    if len(inDegree) != len(originalSeq):
        return False

    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        if len(sources) > 1:
            return False  
        if originalSeq[len(sortedOrder)] != sources[0]:
            return False

        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:  
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    return len(sortedOrder) == len(originalSeq)


if __name__ == "__main__":
    print("Can construct: " +
            str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
            str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
            str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))
