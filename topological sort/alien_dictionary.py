# There is a dictionary containing words from an alien language for which we don’t know the ordering of the letters.
# Write a method to find the correct order of the letters in the alien language.
# It is given that the input is a valid dictionary and there exists an ordering among its letters.

from collections import deque

# O(v+n) time | O(v+n) space
def find_order(words):
    if len(words) == 0:
        return ""

    inDegree = {}
    graph = {}
    for word in words:
        for character in word:
            inDegree[character] = 0
            graph[character] = []

    for i in range(0, len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for j in range(0, min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:
                graph[parent].append(child)
                inDegree[child] += 1
                break

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

    if len(sortedOrder) != len(inDegree):
        return ""

    return "".join(sortedOrder)


if __name__ == "__main__":
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))
