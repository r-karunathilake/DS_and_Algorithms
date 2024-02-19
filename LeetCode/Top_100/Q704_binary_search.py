""" Question 704: Binary Search

Description: Given an array of integers 'nums' which is sorted in ascending 
             order, and an integer target, write a function to search target in 
             nums. If target exists, then return its index. Otherwise, 
             return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
               1 <= nums.length     <= 10^4
           -10^4 <= nums[i], target <  10^4
Note:
    * All the integers in 'nums' are unique
    * 'nums' is sorted in ascending order
"""
from typing import List

def binarySearch(nums: List[int], target: int) -> int:
    l_bound = 0
    u_bound = len(nums) - 1

    while l_bound <= u_bound:
        mid_idx = l_bound + (u_bound - l_bound) // 2

        if nums[mid_idx] == target:
            return mid_idx
        elif nums[mid_idx] > target:
            u_bound = mid_idx - 1
        else:
            l_bound = mid_idx + 1

    return -1
###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestListMerge(unittest.TestCase):
    def test_target_exists(self):
        self.assertEqual(binarySearch([-1, 0, 3, 5, 9, 12], 9), 4)
    
    def test_no_target(self):
        self.assertEqual(binarySearch([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_target_at_end(self):
        self.assertEqual(binarySearch([-1, 0, 3, 5, 9, 12], 12), 5)
    
    def test_target_at_beginning(self):
        self.assertEqual(binarySearch([-1, 0, 3, 5, 9, 12], -1), 0)

if __name__ == "__main__":
    unittest.main() 
