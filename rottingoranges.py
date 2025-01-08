# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  
                elif grid[r][c] == 1:
                    fresh_count += 1

       
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes_elapsed = 0

        while queue:
            r, c, minutes = queue.popleft()
            minutes_elapsed = max(minutes_elapsed, minutes)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, minutes + 1))

        
        return minutes_elapsed if fresh_count == 0 else -1
