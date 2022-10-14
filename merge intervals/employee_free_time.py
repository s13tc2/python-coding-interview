# For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
# Our goal is to find out if there is a free interval that is common to all employees.
# You can assume that each list of employee working hours is sorted on the start time.

# Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
# Output: [3,5]
# Explanation: Both the employees are free between [3,5].

from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex

    def __lt__(self, other):
        return self.interval.start < other.interval.start


# O(nlog(k)) time | O(k) space
def find_employee_free_time(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    min_heap = []
    result = []

    for i in range(n):
        heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

    prevInterval = min_heap[0].interval
    while min_heap:
        qTop = heappop(min_heap)
        if prevInterval.end < qTop.interval.start:
            result.append(Interval(prevInterval.end, qTop.interval.start))
            prevInterval = qTop.interval
        else:
            if prevInterval.end < qTop.interval.end:
                prevInterval = qTop.interval

        employeeSchedule = schedule[qTop.employeeIndex]
        if len(employeeSchedule) > qTop.intervalIndex + 1:
            heappush(
                min_heap,
                EmployeeInterval(
                    employeeSchedule[qTop.intervalIndex + 1],
                    qTop.employeeIndex,
                    qTop.intervalIndex + 1,
                ),
            )
    return result


if __name__ == "__main__":
    input = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end="")
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end="")
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end="")
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()
