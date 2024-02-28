""" Question 169: Majority Element

Description: Given an array nums of size n, return the majority element. The 
             majority element is the element that appears more than ⌊n / 2⌋ 
             times. You may assume that the majority element always exists in 
             the array.

Constraints:
                 1 <= nums.length <= 5 * 10^4
             -10^9 <= nums[i]     <= 10^9
"""

from typing import List

"""The solutions big O is as follows:
   Time Complexity:  O(N)
   Space Complexity: O(1)

   Where N is the number of integers in the array (lists)
"""
def majorityElement(nums: List[int]) -> int:
    majority = None
    count = 0
    for value in nums:
        # A new 'value' must be selected as 'majority' 
        if count == 0: 
            majority = value
        if value == majority:
            count += 1
        # Group cancelling the 'majority' and 'value' counts 
        else: 
            count -= 1
    
    return majority

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestMajorityElement(unittest.TestCase):
    def test_majority(self):
        self.assertEqual(majorityElement([6, 0, 6, 3, 3, 6, 6, 6, 6]), 6)

    def test_majority_small_list(self):
        self.assertEqual(majorityElement([3, 2, 3]), 3)

    def test_another_list(self):
        self.assertEqual(majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)

if __name__ == "__main__":
    unittest.main() 
