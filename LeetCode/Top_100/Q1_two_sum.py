""" Question 1: Two Sum

Description: Given an array of integers nums and an integer target, return 
             indices of the two numbers such that they add up to target. You 
             may assume that each input would have exactly one solution, and 
             you may not use the same element twice.

You can return the answer in any order

Constraints:
               2 <= nums.length <= 10^4
           -10^9 <= nums[i]     <= 10^9
           -10^9 <= target      <= 10^9

Note: strs[i] is only lowercase English letters 
"""
from typing import List

"""First solution using built-in functions
   Time Complexity:  O(2N) -> O(N)
   Space Complexity: O(N)

   Where N is the number of integers in the array (list).
"""
def twoSum(nums: List[int], target: int) -> str:
    numMap = {}
    for idx, num in enumerate(nums): 
        comp = target - num 
        if comp in numMap:
            return [numMap[comp], idx]
        numMap[num] = idx

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestLongestPrefix(unittest.TestCase):
    def test_small_list(self):
        nums = [3, 3]
        self.assertEqual(twoSum(nums, 6), [0, 1])

    def test_medium_list(self):
        nums = [3, 2, 4]
        self.assertEqual(twoSum(nums, 6), [1, 2])

    def test_large_list(self):
        nums = [2, 7, 11, 15]
        self.assertEqual(twoSum(nums, 9), [0, 1])

    def test_large_list2(self):
        nums = [1, 3, 4, 2]
        self.assertEqual(twoSum(nums, 6), [2, 3])


if __name__ == "__main__":
    unittest.main() 
