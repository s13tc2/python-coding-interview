# Given a string, find the length of the longest substring, which has all distinct characters.

# O(N) time | O(K) space or O(1) if there are only 26 distinct characters/alphabet letters


def longest_substring_distinct_characters(s):
    window_start = 0
    char_freq = {}
    max_length = 0

    for window_end in range(len(s)):
        char = s[window_end]
        if char in char_freq:
            window_start = max(window_start, char_freq[char] + 1)
        char_freq[char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == "__main__":
    for s in ["aabccbb", "abbbb", "abccde"]:
        solution = longest_substring_distinct_characters(s)
        print(solution)
