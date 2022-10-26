# Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.

from heapq import *
from collections import deque

# O(nlog(n)) time | O(n) space
def reorganize_string(str, k):
    char_freq = {}
    for char in str:
        char_freq[char] = char_freq.get(char, 0) + 1

    max_heap = []
    for char, freq in char_freq.items():
        heappush(max_heap, (-freq, char))

    result = []
    q = deque()
    while max_heap:
        freq, char = heappop(max_heap)
        result.append(char)
        q.append((freq + 1, char))
        if len(q) == k:
            freq, char = q.popleft()
            if -freq > 0:
                heappush(max_heap, (freq, char))
    return "".join(result) if len(result) == len(str) else ""


if __name__ == "__main__":
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))
