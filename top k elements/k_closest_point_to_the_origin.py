# Given an array of points in a 2D2D plane, find ‘K’ closest points to the origin.

from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "]")

    def distance_from_origin(self):
        return (self.x * self.x) + (self.y * self.y)

    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()


# O(nlog(k)) time | O(k) space
def find_closest_points(points, k):
    max_heap = []

    for i in range(0, k):
        heappush(max_heap, points[i])

    for i in range(k, len(points)):
        if points[i].distance_from_origin() < max_heap[0].distance_from_origin():
            heappop(max_heap)
            heappush(max_heap, points[i])

    return max_heap


if __name__ == "__main__":
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ")
    for point in result:
        point.print_point()
