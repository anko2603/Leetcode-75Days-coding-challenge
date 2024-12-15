# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
# Example 1:
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_count = {}

        
        for row in grid:
            row_tuple = tuple(row)
            row_count[row_tuple] = row_count.get(row_tuple, 0) + 1

        count = 0


        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))
            if col_tuple in row_count:
                count += row_count[col_tuple]

        return count
 