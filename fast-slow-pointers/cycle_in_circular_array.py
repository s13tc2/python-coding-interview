# We are given an array containing positive and negative numbers.
# Suppose the array contains a number ‘M’ at a particular index.
# Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices.
# You should assume that the array is circular which means two things:

# If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
# If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
# Write a method to determine if the array has a cycle.
# The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

# Input: [1, 2, -1, 2, 2]
# Output: true
# Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

# O(N^2) time | O(1) space
def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        slow, fast = i, i
        is_forward = arr[i] >= 0

        while True:
            slow = get_next_valid_index(arr, is_forward, slow)
            fast = get_next_valid_index(arr, is_forward, fast)
            if fast != -1:
                fast = get_next_valid_index(arr, is_forward, fast)
            if slow == -1 or fast == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True
    return False


def get_next_valid_index(arr, is_forward, index):
    direction = arr[index] >= 0

    if direction != is_forward:
        return -1

    next_index = (index + arr[index]) % len(arr)
    if next_index == index:
        next_index = -1

    return next_index


if __name__ == "__main__":
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))
