# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N!N! permutations (or anagrams) of a string having NNN characters. For example, here are the six anagrams of the string “abc”:

#     1. abc
#     2. acb
#     3. bac
#     4. bca
#     5. cab
#     6. cba

# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# O(N+M) time | O(M) space
def string_anagrams(s, pattern):
    result_indices = []

    char_freq = {}
    for char in pattern:
        char_freq[char] = char_freq.get(char, 0) + 1

    window_start = 0
    matched = 0

    for window_end in range(len(s)):
        char = s[window_end]
        if char in char_freq:
            char_freq[char] -= 1
            if char_freq[char] == 0:
                matched += 1

        if matched == len(char_freq):
            result_indices.append(window_start)

        if window_end >= len(pattern) - 1:
            char = s[window_start]
            window_start += 1
            if char in char_freq:
                if char_freq[char] == 0:
                    matched -= 1
                char_freq[char] += 1

    return result_indices


if __name__ == "__main__":
    solution = string_anagrams("ppqp", "pq")
    print(solution)
    solution = string_anagrams("abbcabc", "abc")
    print(solution)
