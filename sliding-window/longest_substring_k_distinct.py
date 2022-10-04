# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# O(N) time | O(K) space
def longest_substring_k_distinct(s, k):
    char_freq = {}
    window_start = 0
    max_length = 0

    for window_end in range(len(s)):
        char = s[window_end]
        char_freq[char] = char_freq.get(char, 0) + 1

        if len(char_freq) > k:
            char = s[window_start]
            char_freq[char] -= 1
            if char_freq[char] == 0:
                del char_freq[char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == "__main__":
    solution = longest_substring_k_distinct("araaci", 2)
    print(solution)
    solution = longest_substring_k_distinct("araaci", 1)
    print(solution)
    solution = longest_substring_k_distinct("cbbebi", 3)
    print(solution)
