# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

# using for loop
# O(N) time | O(N) space
def square_sorted_array(arr):
    result = [0 for x in arr]
    left = 0
    right = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        if abs(arr[left]) < abs(arr[right]):
            sq = arr[right]
            right -= 1
        else:
            sq = arr[left]
            left += 1
        result[i] = sq * sq
    return result


# using while loop
# O(N) time | O(N) space
def square_sorted_array_2(arr):
    result = [0 for x in arr]
    left, right = 0, len(arr) - 1
    n = len(arr) - 1
    while left <= right:
        if abs(arr[left]) < abs(arr[right]):
            result[n] = arr[right] * arr[right]
            right -= 1
        else:
            result[n] = arr[left] * arr[left]
            left += 1
        n -= 1
    return result


if __name__ == "__main__":
    solution = square_sorted_array([-2, -1, 0, 2, 3])
    print(solution)
    solution = square_sorted_array_2([-2, -1, 0, 2, 3])
    print(solution)
