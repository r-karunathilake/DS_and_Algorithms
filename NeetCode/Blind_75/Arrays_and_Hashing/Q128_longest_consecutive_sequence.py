""" Question 128: Longest Consecutive Sequence 

Description: Given an unsorted array of integers nums, return the length of 
             the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Constraints:
               0 <= nums.length <= 10^5
           -10^9 <= nums[i]     <= 10^9
"""


""" 
   Time complexity: O(N)
   Space complexity: O(N)
"""
def longestConsecutive(nums: list[int]) -> list[int]:
    if not nums: 
        return 0
    
    nums = set(nums)  # For efficient look-up & duplicate elimination
    current_max_seq = 0

    for num in nums:
        current_num = num
        if num - 1 not in nums: # Start of a new sequence
            current_seq = 1

            while current_num + 1 in nums:
                current_num += 1
                current_seq += 1
            
            current_max_seq = max(current_max_seq, current_seq)

    return current_max_seq
    
###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestGroupAnagrams(unittest.TestCase):
    def test_one(self):
        nums = [100,4,200,1,3,2]
        self.assertEqual(longestConsecutive(nums), 4)

    def test_two(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        self.assertEqual(longestConsecutive(nums), 9)

if __name__ == "__main__":
    unittest.main() 
