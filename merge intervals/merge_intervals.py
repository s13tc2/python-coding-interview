# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


# O(nlog(n)) time | O(n) space
def merge(intervals):
    if not intervals:
        return intervals

    merged = []
    sorted_intervals = sorted(intervals, key=lambda x: x.start)
    current_interval = sorted_intervals[0]
    merged.append(current_interval)

    for next_interval in sorted_intervals:
        next_interval_start, next_interval_end = next_interval.start, next_interval.end
        _, current_interval_end = current_interval.start, current_interval.end

        if current_interval_end >= next_interval_start:
            current_interval.end = max(current_interval_end, next_interval_end)
        else:
            current_interval = next_interval
            merged.append(current_interval)
    return merged


if __name__ == "__main__":
    print("Merged intervals: ", end="")
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end="")
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end="")
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()
