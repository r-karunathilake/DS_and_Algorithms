""" Question 136: Single Number

Description: Given a non-empty array of integers nums, every element appears 
             twice except for one. Find that single one. You must implement a 
             solution with a linear runtime complexity and use only constant 
             extra space.

Constraints:
                 1 <= nums.length <= 3 * 10^4
         -3 * 10^4 <= nums[i]     <= 3 * 10^4
"""

from typing import List

def singleNumber(nums: List[int]) -> int:
    single = 0
    for value in nums:
        # XOR of a number with itself results in 0
        single ^= value

    return single

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestSingleNumber(unittest.TestCase):
    def test_majority(self):
        self.assertEqual(singleNumber([2, 2, 1]), 1)

    def test_majority_one(self):
        self.assertEqual(singleNumber([4, 2, 1, 2, 4]), 1)
    
    def test_majority_four(self):
        self.assertEqual(singleNumber([4, 1, 2, 1, 2]), 4)

if __name__ == "__main__":
    unittest.main() 
