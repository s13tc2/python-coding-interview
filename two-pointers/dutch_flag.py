# Given an array containing 0s, 1s and 2s, sort the array in-place. Y
# ou should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue;
# and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

# Input: [1, 0, 2, 1, 0]
# Output: [0, 0, 1, 1, 2]

# O(N) time | O(1) space
def dutch_flag_sort(arr):
    start, end = 0, len(arr) - 1
    i = 0
    while i <= end:
        if arr[i] == 0:
            arr[start], arr[i] = arr[i], arr[start]
            start += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1


if __name__ == "__main__":
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)
