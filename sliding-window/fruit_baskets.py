# You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

# You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

#     1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
#     2. You can start with any tree, but you can’t skip a tree once you have started.
#     3. You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both baskets.

# O(N) time | O(1) space
def fruit_into_baskets(fruits):
    window_start = 0
    max_length = 0
    char_freq = {}

    for window_end in range(len(fruits)):
        char = fruits[window_end]
        char_freq[char] = char_freq.get(char, 0) + 1

        if len(char_freq) > 2:
            char = fruits[window_start]
            char_freq[char] -= 1
            if char_freq[char] == 0:
                del char_freq[char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == "__main__":
    solution = fruit_into_baskets(["A", "B", "C", "A", "C"])
    print(solution)
    solution = fruit_into_baskets(["A", "B", "C", "B", "B", "C"])
    print(solution)
