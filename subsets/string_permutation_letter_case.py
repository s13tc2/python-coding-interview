# Given a string, find all of its permutations preserving the character sequence but changing case.

# Input: "ad52"
# Output: "ad52", "Ad52", "aD52", "AD52"

# Input: "ab7c"
# Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"


def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)
    for i in range(len(str)):
        char = str[i]
        if char.isalpha():
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                chs[i] = chs[i].swapcase()
                permutations.append("".join(chs))
    return permutations


if __name__ == "__main__":
    print(
        "String permutations are: " + str(find_letter_case_string_permutations("ad52"))
    )
    print(
        "String permutations are: " + str(find_letter_case_string_permutations("ab7c"))
    )
