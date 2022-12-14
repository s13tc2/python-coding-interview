# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits,
# leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

# Input: 23   
# Output: true (23 is a happy number)  
# Explanations: Here are the steps to find out that 23 is a happy number:

# O(log(n)) time | O(1) space
def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_square(slow)
        fast = find_square(find_square(fast))
        if slow == fast:
            break
    return slow == 1


def find_square(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num /= 10
    return _sum


if __name__ == "__main__":
    print(find_happy_number(23))
    print(find_happy_number(12))
