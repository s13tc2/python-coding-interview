# Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.

# Input: "1+2*3"
# Output: 7, 9
# Explanation: 1+(2*3) => 7 and (1+2)*3 => 9

# Input: "2*3-4-5"
# Output: 8, -12, 7, -7, -3
# Explanation: 2*(3-(4-5)) => 8, 2*(3-4-5) => -12, 2*3-(4-5) => 7, 2*(3-4)-5 => -7, (2*3)-4-5 => -3

# O(n*2^n) time | O(2^n) space
def diff_ways_to_evaluate_expression(input):
    result = []
    if "+" not in input and "-" not in input and "*" not in input:
        result.append(int(input))
    else:
        for i in range(len(input)):
            char = input[i]
            if not char.isdigit():
                left = diff_ways_to_evaluate_expression(input[0:i])
                right = diff_ways_to_evaluate_expression(input[i + 1 :])
                for part1 in left:
                    for part2 in right:
                        if char == "+":
                            result.append(part1 + part2)
                        elif char == "-":
                            result.append(part1 - part2)
                        elif char == "*":
                            result.append(part1 * part2)
    return result


if __name__ == "__main__":
    print("Expression evaluations: " + str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " + str(diff_ways_to_evaluate_expression("2*3-4-5")))
