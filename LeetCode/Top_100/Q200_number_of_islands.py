""" Question 200: Number of Islands  

Description: Given an m x n 2D binary 'grid' which represents a map of '1's (land)
             and '0's (water), return the number of islands.

             An island is surrounded by water and is formed by connecting adjacent 
             lands horizontally or vertically. You may assume all four edges of the 
             grid are all surrounded by water.

Constraints:
                 1 <= m, n <= 300
                 cell.val == '0' or '1' 
"""

from typing import Optional, List

"""This is an depth-first-search approach to this problem. The big O 
   of this solution is as follows:
    
   Time complexity: O(M x N)
   Space complexity: O(1)

   Where M and N are the dimentions of the grid.
"""

def numIslands(grid: List[List[str]]) -> int:

    def explorerIsland(row: int, column: int) -> None:
        # Check row bounds 
        if row < 0 or row >= len(grid):
            return None

        # Check column bounds 
        if column < 0 or column >= len(grid[0]):
            return None 

        # Check if valid grid cell value
        if grid[row][column] == "0":
            return None

        # Mark current cell as visited 
        grid[row][column] = "0"

        # Find other cells that are part of the current island
        explorerIsland(row - 1, column) # Top cell
        explorerIsland(row + 1, column) # Bottom cell
        explorerIsland(row, column - 1) # Left cell
        explorerIsland(row, column + 1) # Right cell

    num_islands = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == "0":
                continue
            
            # Found an island! 
            num_islands += 1
            explorerIsland(row, column)

    return num_islands

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestIslandCounter(unittest.TestCase):
    def test_no_islands(self):
        grid = [["0","0","0","0","0"],
                ["0","0","0","0","0"],
                ["0","0","0","0","0"],
                ["0","0","0","0","0"]]
        self.assertEqual(numIslands(grid), 0)
    
    def test_one_islands(self):
        grid = [["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]
        self.assertEqual(numIslands(grid), 1)
    
    def test_three_islands(self):
        grid = [["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]]
        self.assertEqual(numIslands(grid), 3)

if __name__ == '__main__':
    unittest.main()
