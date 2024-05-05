""" Question 238: Product of Array Except Self

Description: Given an integer array nums, return an array answer such that 
             answer[i] is equal to the product of all the elements of nums 
             except nums[i].

Constraints:
               2 <= nums.length <= 10^5
             -30 <= nums[i]     <= 30
"""


""" Solution #1: 

   Time complexity: O(N)
   Space complexity: O(1)
"""
def productExceptSelf(nums: list[int]) -> list[int]:
    length = len(nums)
    result = [1] * length

    # Calculate the product of numbers left of the current index i 
    # We start at index 1 b/c no elements left of the i = 0 (result is defaulted
    # to 1)

    # E.g. nums = [1, 2, 3, 4], result = [1, 1, 1, 1]
    for idx in range(1, length):
        result[idx] = result[idx - 1] * nums[idx - 1]

    # E.g. result = [1, 1, 2, 6] <--- left product for each position 

    right_product = 1
    for idx in range(length - 1, -1 , -1):
        result[idx] *= right_product
        right_product *= nums[idx]

    # E.g. result = [24, 12, 8, 6]
    return result 
    
###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestGroupAnagrams(unittest.TestCase):
    def test_one(self):
        nums = [1,2,3,4]
        self.assertEqual(productExceptSelf(nums), [24,12,8,6])

    def test_two(self):
        nums = [-1,1,0,-3,3]
        self.assertEqual(productExceptSelf(nums), [0,0,9,0,0])

if __name__ == "__main__":
    unittest.main() 
