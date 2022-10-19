# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

# Input: N=2
# Output: (()), ()()

# Input: N=3
# Output: ((())), (()()), (())(), ()(()), ()()()

from collections import deque


class ParenthesesString:
    def __init__(self, str, open_count, close_count):
        self.str = str
        self.open_count = open_count
        self.close_count = close_count


# O(n*2^n) time | O(n*2^n) space
def generate_valid_parentheses(num):
    q = deque()
    q.append(ParenthesesString("", 0, 0))
    result = []
    while q:
        ps = q.popleft()
        if ps.open_count == num and ps.close_count == num:
            result.append(ps.str)
        else:
            if ps.open_count < num:
                q.append(
                    ParenthesesString(ps.str + "(", ps.open_count + 1, ps.close_count)
                )
            if ps.close_count < ps.open_count:
                q.append(
                    ParenthesesString(ps.str + ")", ps.open_count, ps.close_count + 1)
                )
    return result


if __name__ == "__main__":
    print(
        "All combinations of balanced parentheses are: "
        + str(generate_valid_parentheses(2))
    )
    print(
        "All combinations of balanced parentheses are: "
        + str(generate_valid_parentheses(3))
    )
