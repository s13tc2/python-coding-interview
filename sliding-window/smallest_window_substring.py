# Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"

# O(N+M) time | O(M) space
def smallest_window_substring(s, pattern):
    char_freq = {}
    for char in pattern:
        char_freq[char] = char_freq.get(char, 0) + 1

    substr_start = 0
    window_start = 0
    matched = 0
    min_length = len(s) + 1

    for window_end in range(len(s)):
        char = s[window_end]
        if char in char_freq:
            char_freq[char] -= 1
            if char_freq[char] >= 0:
                matched += 1

        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            char = s[window_start]
            window_start += 1
            if char in char_freq:
                if char_freq[char] == 0:
                    matched -= 1
                char_freq[char] += 1

    if min_length > len(s):
        return ""

    return s[substr_start : substr_start + min_length]


if __name__ == "__main__":
    solution = smallest_window_substring("aabdec", "abc")
    print(solution)
    solution = smallest_window_substring("aabdec", "abac")
    print(solution)
    solution = smallest_window_substring("abdbca", "abc")
    print(solution)
    solution = smallest_window_substring("adcad", "abc")
    print(solution)
