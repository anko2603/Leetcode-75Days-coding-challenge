# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
# Example 1:
# Input
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# Output
# [null, null, 1, 2, 3, null, 1, 4, 5]
import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1  
        self.heap = []
        self.set = set()  

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.set.remove(smallest)          
            return smallest
        else:
            smallest = self.current
            self.current += 1                  
            return smallest

    def addBack(self, num: int) -> None:
      
        if num < self.current and num not in self.set:
            heapq.heappush(self.heap, num)  
            self.set.add(num)               
