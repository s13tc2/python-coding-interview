# You are given a list of tasks that need to be run, in any order, on a server.
# Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can’t be run again.
# If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

# If at any time the server can’t execute any task then it must stay idle.

from heapq import *

# O(nlog(n)) time | O(n) space
def schedule_tasks(tasks, k):
    intervalCount = 0
    char_freq = {}
    for char in tasks:
        char_freq[char] = char_freq.get(char, 0) + 1

    max_heap = []
    for char, freq in char_freq.items():
        heappush(max_heap, (-freq, char))

    while max_heap:
        n = k + 1
        waitList = []
        while max_heap and n > 0:
            intervalCount += 1
            freq, char = heappop(max_heap)
            if -freq > 1:
                waitList.append((freq + 1, char))
            n -= 1

        for freq, char in waitList:
            heappush(max_heap, (freq, char))

        if max_heap:
            intervalCount += n

    return intervalCount


if __name__ == "__main__":
    print(
        "Minimum intervals needed to execute all tasks: "
        + str(schedule_tasks(["a", "a", "a", "b", "c", "c"], 2))
    )
    print(
        "Minimum intervals needed to execute all tasks: "
        + str(schedule_tasks(["a", "b", "a"], 3))
    )
