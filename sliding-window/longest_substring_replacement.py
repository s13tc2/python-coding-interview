# Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter,
# find the length of the longest substring having the same letters after replacement.

# O(N) time | O(26) or O(1) space
def longest_substring_replacement(s, k):
    char_freq = {}
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0

    for window_end in range(len(s)):
        char = s[window_end]
        char_freq[char] = char_freq.get(char, 0) + 1
        max_repeat_letter_count = max(max_repeat_letter_count, char_freq[char])

        if window_end - window_start + 1 - max_repeat_letter_count > k:
            char = s[window_start]
            char_freq[char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == "__main__":
    solution = longest_substring_replacement("aabccbb", 2)
    print(solution)
    solution = longest_substring_replacement("abbcb", 1)
    print(solution)
    solution = longest_substring_replacement("abccde", 1)
    print(solution)
