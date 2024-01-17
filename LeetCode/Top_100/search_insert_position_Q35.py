""" Question 35: Search Insert Position 

Description: Given a sorted array of distinct integers and a target value, 
             return the index if the target is found. If not, return the 
             index where it would be if it were inserted in order.

             You must write an algorithm with O(log n) runtime complexity.

Constraints:
                 1 <= nums.length <= 10^4
             -10^4 <= node.val    <= 10^4
             -10^4 <= target      <= 10^4

Note: contains distinct values sorted in ascending order.
"""
from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    if not nums:
        return 0 # List is empty, return index 0 

    # Let's try binary search 
    t_lim = len(nums) - 1
    b_lim= 0 # Start at the middle index

    while b_lim <= t_lim:
        mid = (b_lim + t_lim) // 2

        if nums[mid] < target:
            b_lim = mid + 1 
        elif nums[mid] > target:
            t_lim = mid - 1
        else:
            return mid 

    return b_lim 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestBinarySearch(unittest.TestCase):
    def test_empty_list(self):
       nums = []
       self.assertEqual(searchInsert(nums, -1), 0)

    def test_list(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(searchInsert(nums, 5), 2)

    def test_target_not_found(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(searchInsert(nums, 2), 1)
    
    def test_target_not_found_end(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(searchInsert(nums, 7), 4)

if __name__ == '__main__':
    unittest.main()
