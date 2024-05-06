""" Question 15: 3Sum

Description: Given an integer array nums, return all the triplets [nums[i], 
             nums[j], nums[k]] such that i != j, i != k, and j != k, and 
             nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:
               3 <= nums.length <= 3000
           -10^5 <= nums[i]     <= 10^5

           


           
   Time complexity: O(N^2)
   Space complexity: O(N)

   Where N in the number of values in 'nums' 
"""
from itertools import combinations

def threeSum(nums: list[int]) -> list[list[int]]:
    result = list()

    n, p, z =[], [], []
    # Split nums to negative, positive and zero lists 
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else: # num == 0
            z.append(num)

    # Create N, P set for O(1) lookup 
    N, P = set(n), set(p)

    if z:
        for num in P:
            if -num in N:
                result.append([-num, 0, num])
    
        # If there is atleast 3 zeros 
        if len(z) >= 3:
            result.append([0, 0, 0])


    # For all pairs of negative numbers, check for positive complement 
    for n1, n2 in combinations(n, 2):
        complement = -1 * (n1 + n2)
        if complement in P:
            result.append(sorted([n1, n2, complement]))

    # For all pairs of positive numbers, check for negative complement 
    for p1, p2 in combinations(p, 2):
        complement = -1 * (p1 + p2)
        if complement in N:
            result.append(sorted([p1, p2, complement]))

    return result 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestGroupAnagrams(unittest.TestCase):
    def test_one(self):
        nums = [-1,0,1,2,-1,-4]
        solution = [[-1,0,1],[-1,-1,2]]
        self.assertEqual(threeSum(nums), solution)

    def test_two(self):
        nums = [0,1,1]
        solution = []
        self.assertEqual(threeSum(nums), solution)

    def test_three(self):
        nums = [0,0,0]
        solution = [[0,0,0]]
        self.assertEqual(threeSum(nums), solution)

    def test_four(self):
        nums = [0,0,0,0]
        solution = [[0,0,0]]
        self.assertEqual(threeSum(nums), solution)

    def test_five(self):
        nums = [-1,0,1,0]
        solution = [[-1,0,1]]
        self.assertEqual(threeSum(nums), solution)

if __name__ == "__main__":
    unittest.main() 
