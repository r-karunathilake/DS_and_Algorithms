""" Question 46: Permutations 

Description: Given an array nums of distinct integers, return all the 
             possible permutations. You can return the answer in any order.
Constraints:
               1 <= nums.length <= 6
             -10 <= nums[i]     <= 10

Note: all the integers of 'nums' are unique
"""

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    n = len(nums)

    # Base case 
    if n == 1: # Only one permutation possible 
        return [nums] 
    
    perms = list()

    for idx, val in enumerate(nums):
        remaining_nums = nums[0:idx] + nums[idx + 1:]
        # Generate all permutations with 'val' as the first element 
        for permutation in permute(remaining_nums):
            perms.append([val] + permutation)

    return perms 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestPermutation(unittest.TestCase):
    def test_one(self):
        nums = [1, 2, 3]
        expected_result = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(permute(nums), expected_result)

    def test_two(self):
        nums = [0, 1]
        expected_result = [[0, 1],[1,0]]
        self.assertEqual(permute(nums), expected_result)

    def test_three(self):
        nums = [1]
        expected_result = [[1]]
        self.assertEqual(permute(nums), expected_result)

if __name__ == "__main__":
    unittest.main() 


