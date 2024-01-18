""" Question 78: Subsets

Description: Given an integer array nums of unique elements, 
             return all possible subsets(the power set).
             The solution set must not contain duplicate 
             subsets. Return the solution in any order.
Constraints:
               1 <= nums.length <= 10
             -10 <= nums[i]     <= 10

Note: all the integers of 'nums' are unique
"""

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    def backtrack(start, subset):
        # Add the current subset to results 
        result.append(subset[:])
        
        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop() # Undo the choice made in the previous step 

    # Initially an empty list 
    result = []

    # Start the backtracking process 
    backtrack(0, [])

    return result

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestPermutation(unittest.TestCase):
    def test_one(self):
        nums = [1, 2, 3]
        expected_result = [[],[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertCountEqual(subsets(nums), expected_result)

    def test_two(self):
        nums = [0, 1]
        expected_result = [[], [0], [1], [0, 1]]
        self.assertCountEqual(subsets(nums), expected_result)

    def test_three(self):
        nums = [0]
        expected_result = [[], [0]]
        self.assertCountEqual(subsets(nums), expected_result)

if __name__ == "__main__":
    unittest.main() 
