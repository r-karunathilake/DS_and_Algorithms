""" Question 283: Move Zeroes 

Description: Given an integer array 'nums', move all 0's to the end of it 
             while mainting the relative order of the non-zero elements. 
Constraints:
               1 <= nums.length <= 10^4
           -2^31 <= nums[i]     <= 2^31 - 1

Note: you must do this in-place without making a copy of the array.
"""

from typing import List

"""First solution using big O is as follows:
   Time Complexity:  O(N^2)
   Space Complexity: O(1)

   Where N is the number of integers in the array
"""
def moveZeroesBrute(nums: List[int]) -> None:
    for idx in range(len(nums)):
        if nums[idx] != 0:
            continue 
        nums.append(nums.pop(idx)) 

"""Second solution using big O is as follows:
   Time Complexity:  O(N)
   Space Complexity: O(1)

   Where N is the number of integers in the array
"""
def moveZeroes(nums: List[int]) -> None:
    # Guess non-zero index 0 
    non_zero_idx = 0
    for idx in range(len(nums)):
        # Move the non-zero element to the front 
        if nums[idx] != 0:
            nums[non_zero_idx], nums[idx] = nums[idx], nums[non_zero_idx]
            non_zero_idx += 1
        
###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestMoveZeroes(unittest.TestCase):
    def test_list_with_zeroes(self):
        nums = [0, 1, 25, 0, 1, 6, 8, 0]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 25, 1, 6, 8, 0, 0, 0])
    
    def test_one_item_list(self):
        nums = [0]
        moveZeroes(nums)
        self.assertEqual(nums, [0])

if __name__ == "__main__":
    unittest.main() 
