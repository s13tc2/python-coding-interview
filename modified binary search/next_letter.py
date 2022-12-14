# Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.

# Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter.
# This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.

# Write a function to return the next letter of the given ‘key’.

# O(log(n)) time | O(1) space
def search_next_letter(letters, key):
    n = len(letters)
    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if letters[mid] <= key:
            start = mid + 1
        else:
            end = mid - 1
    return letters[start % n]


if __name__ == "__main__":
    print(search_next_letter(["a", "c", "f", "h"], "f"))
    print(search_next_letter(["a", "c", "f", "h"], "b"))
    print(search_next_letter(["a", "c", "f", "h"], "m"))
