# Design a class that simulates a Stack data structure, implementing the following two operations:

#     1. push(int num): Pushes the number ‘num’ on the stack.
#     2. pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.

from heapq import *


class Element:
    def __init__(self, num, freq, seqNum):
        self.num = num
        self.freq = freq
        self.seqNum = seqNum

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq > other.freq
        return self.seqNum > other.seqNum


# O(log(n)) time | O(n) space
class FrequencyStack:
    numFreq = {}
    maxHeap = []
    seqNum = 0

    def push(self, num):
        # TODO: Write your code here
        self.numFreq[num] = self.numFreq.get(num, 0) + 1
        heappush(self.maxHeap, Element(num, self.numFreq[num], self.seqNum))
        self.seqNum += 1

    def pop(self):
        num = heappop(self.maxHeap).num
        if self.numFreq[num] > 1:
            self.numFreq[num] -= 1
        else:
            del self.numFreq[num]

        return num


if __name__ == "__main__":
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())
