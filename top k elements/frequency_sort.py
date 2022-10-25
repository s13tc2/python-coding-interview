# Given a string, sort it based on the decreasing frequency of its characters.
from heapq import *

# O(nlog(n)) time or O(dlog(d)) where d is number of distinct char. in the input string | O(n) space
def sort_character_by_frequency(str):
    char_freq = {}
    for char in str:
        char_freq[char] = char_freq.get(char, 0) + 1

    max_heap = []
    for char, freq in char_freq.items():
        heappush(max_heap, (-freq, char))

    result = []
    while max_heap:
        freq, char = heappop(max_heap)
        for _ in range(-freq):
            result.append(char)

    return "".join(result) if len(result) == len(str) else ""


if __name__ == "__main__":
    print(
        "String after sorting characters by frequency: "
        + sort_character_by_frequency("Programming")
    )
    print(
        "String after sorting characters by frequency: "
        + sort_character_by_frequency("abcbab")
    )
