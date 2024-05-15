""" Question 153: Find Minimum in Rotated Sorted Array

Description: Suppose an array of length n sorted in ascending order is rotated 
             between 1 and n times. For example, the array 
             nums = [0,1,2,4,5,6,7] might become:

                [4,5,6,7,0,1,2] if it was rotated 4 times.
                [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results 
in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum 
element of this array.

You must write an algorithm that runs in O(log n) time.

Constraints:
                    n == nums.length
                    1 <= n       <= 5000
                -5000 <= nums[i] <= 5000

    - All the integers of 'nums' are unique.
    - 'nums' is sorted and rotated between 1 and n times.
"""

def findMin(nums: list[int]) -> int:
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            # No -1 b/c what if the middle index is the smallest (see test case #1)
            r = mid  

    return nums[l]

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestRotatedMin(unittest.TestCase):
    def test_one(self):
        nums = [3, 4, 0, 1, 2]
        solution = 0
        self.assertEqual(findMin(nums), solution)
    
    def test_two(self):
        nums = [3,4,5,1,2]
        solution = 1
        self.assertEqual(findMin(nums), solution)

    def test_three(self):
        nums = [4,5,6,7,0,1,2]
        solution = 0
        self.assertEqual(findMin(nums), solution)

    def test_four(self):
        nums = [11,13,15,17]
        solution = 11
        self.assertEqual(findMin(nums), solution)

if __name__ == "__main__":
    unittest.main() 
