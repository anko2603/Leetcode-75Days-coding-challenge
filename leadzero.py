# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.
# Example 1:
# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
from collections import defaultdict, deque
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, True))
            graph[v].append((u, False))
        

        queue = deque([0])
        visited = set()
        visited.add(0)
        changes = 0
        
        while queue:
            current = queue.popleft()
            for neighbor, is_outward in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if is_outward:
                        changes += 1
                    queue.append(neighbor)
        
        return changes
