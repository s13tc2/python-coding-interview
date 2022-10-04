# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

#     1. abc
#     2. acb
#     3. bac
#     4. bca
#     5. cab
#     6. cba

# If a string has ‘n’ distinct characters, it will have n! permutations.

# O(N+M) time | O(M) space
def find_permutation(s, pattern):
    char_freq = {}

    for char in pattern:
        char_freq[char] = char_freq.get(char, 0) + 1

    window_sum = 0
    window_start = 0
    matched = 0

    for window_end in range(len(s)):
        char = s[window_end]
        if char in char_freq:
            char_freq[char] -= 1
            if char_freq[char] == 0:
                matched += 1

        if matched == len(char_freq):
            return True

        if window_end >= len(pattern) - 1:
            char = s[window_start]
            window_start += 1
            if char in char_freq:
                if char_freq[char] == 0:
                    matched -= 1
                char_freq[char] += 1

    return False


if __name__ == "__main__":
    solution = find_permutation("oidbcaf", "abc")
    print(solution)
    solution = find_permutation("odicf", "dc")
    print(solution)
    solution = find_permutation("bcdxabcdy", "bcdyabcdx")
    print(solution)
    solution = find_permutation("aaacb", "abc")
    print(solution)
