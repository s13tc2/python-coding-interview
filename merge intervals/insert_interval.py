# Given a list of non-overlapping intervals sorted by their start time,
# insert a given interval at the correct position and merge all necessary
# intervals to produce a list that has only mutually exclusive intervals.

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

# O(nlog(n)) time | O(n) space
def insert_interval(intervals, new_interval):
    merged = []
    intervals.sort()
    i = 0
    start, end = 0, 1

    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][start] < new_interval[end]:
        new_interval[start] = min(new_interval[start], intervals[i][start])
        new_interval[end] = max(new_interval[end], intervals[i][end])
        i += 1

    merged.append(new_interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged


if __name__ == "__main__":
    print(
        "Intervals after inserting the new interval: "
        + str(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 6]))
    )
    print(
        "Intervals after inserting the new interval: "
        + str(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10]))
    )
    print(
        "Intervals after inserting the new interval: "
        + str(insert_interval([[2, 3], [5, 7]], [1, 4]))
    )
