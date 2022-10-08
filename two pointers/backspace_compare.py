# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

# O(N+M) time | O(1) space
def backspace_compare(s1, s2):
    index1 = len(s1) - 1
    index2 = len(s2) - 1
    while index1 >= 0 or index2 >= 0:
        i1 = get_next_valid_index(s1, index1)
        i2 = get_next_valid_index(s2, index2)

        if i1 <= 0 and i2 <= 0:
            return True
        elif i1 <= 0 or i2 <= 0:
            return False
        elif s1[i1] != s2[i2]:
            return False

        index1 = i1 - 1
        index2 = i2 - 1
    return False


def get_next_valid_index(s, index):
    backspace_count = 0
    while index >= 0:
        if s[index] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break

        index -= 1
    return index


if __name__ == "__main__":
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))
