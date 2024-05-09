""" Question 33: Search in Rotated Sorted Array

Description: There is an integer array nums sorted in ascending order 
             (with distinct values). Prior to being passed to your function, 
             nums is possibly rotated at an unknown pivot index k 
             (1 <= k < nums.length) such that the resulting array is 
             [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
             (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at 
             pivot index 3 and become [4,5,6,7,0,1,2]. Given the array nums 
             after the possible rotation and an integer target, return the 
             index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
               1 <= nums.length <= 5000
           -10^4 <= nums[i]     <= 10^4
           -10^4 <= target      <= 10^4

All values of nums are unique.
nums is an ascending array that is possibly rotated.
"""

"""The solutions big O is as follows:
   
   Time Complexity:  O(LogN)
   Space Complexity: O(1)

   Where N is the number of integers in the array. 
"""
def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m_idx = (l + r) // 2
        m_val, l_val, r_val = nums[m_idx], nums[l], nums[r]

        if m_val == target:
            return m_idx 
        
        # if k < len(nums) // 2, the first half of the array 
        # should be sorted. The value at index 0 of 'nums' is the pivot value.
        if l_val <= m_val:
            if l_val <= target < m_val: # Target has to be in the left half
                r = m_idx - 1
            else:
                l = m_idx + 1 # Target has to be in the right half
        else:
            if m_val < target <= r_val:
                l = m_idx + 1
            else:
                r = m_idx - 1

    return -1 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestSearch(unittest.TestCase):
    def test_one(self):
        nums = [4,5,6,7,0,1,2]
        self.assertEqual(search(nums, 0), 4)

    def test_two(self):
        nums = [4,5,6,7,0,1,2]
        self.assertEqual(search(nums, 3), -1)

    def test_three(self):
        nums = [1]
        self.assertEqual(search(nums, 0), -1)

if __name__ == "__main__":
    unittest.main() 
