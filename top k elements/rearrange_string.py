# Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

from heapq import *

# O(nlog(n)) time | O(n) space
def rearrange_string(str):
    char_freq = {}
    for char in str:
        char_freq[char] = char_freq.get(char, 0) + 1

    max_heap = []
    for char, freq in char_freq.items():
        heappush(max_heap, (-freq, char))

    result = []
    prevChar, prevFreq = None, 0
    while max_heap:
        freq, char = heappop(max_heap)
        if prevChar and -prevFreq > 0:
            heappush(max_heap, (prevFreq, prevChar))
        result.append(char)
        prevChar = char
        prevFreq = freq + 1

    return "".join(result) if len(result) == len(str) else ""


if __name__ == "__main__":
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))
