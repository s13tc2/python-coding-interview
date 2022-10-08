# Given a string and a list of words, find all the starting indices of substrings in the given string
# that are a concatenation of all the given words exactly once without any overlapping of words.
# It is given that all words are of the same length.

# Input: String="catfoxcat", Words=["cat", "fox"]
# Output: [0, 3]
# Explanation: The two substring containing both the words are "catfox" & "foxcat".

# O(N*M*Len) time | O(M+N) space
def word_concat(s, words):
    word_freq = {}
    result_indices = []

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(s) - words_count * word_length) + 1):
        words_seen = {}
        for j in range(0, words_count):
            next_index = i + j * word_length
            word = s[next_index : next_index + word_length]

            if word not in word_freq:
                break

            words_seen[word] = words_seen.get(word, 0) + 1

            if words_seen[word] > word_freq.get(word, 0):
                break

            if j + 1 == words_count:
                result_indices.append(i)

    return result_indices


if __name__ == "__main__":
    solution = word_concat("catfoxcat", ["cat", "fox"])
    print(solution)
    solution = word_concat("catcatfoxfox", ["cat", "fox"])
    print(solution)
