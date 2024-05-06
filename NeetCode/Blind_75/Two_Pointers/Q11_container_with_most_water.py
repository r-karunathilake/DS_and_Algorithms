""" Question 11: Container With Most Water

Description: You are given an integer array height of length n. There are n 
             vertical lines drawn such that the two endpoints of the ith line 
             are (i, 0) and (i, height[i]). Find two lines that together with 
             the x-axis form a container, such that the container contains the 
             most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Constraints:
               n == height.length 
               2 <= n <= 10^5
               0 <= height[i]     <= 10^4

           
           
   Time complexity: O(N)
   Space complexity: O(1)

   Where N in the number of values in 'height' 
"""
def maxArea(height: list[int]) -> int:
    left = 0 
    right  = len(height) - 1

    max_water = 0

    while left <= right:
        # Calculate the area 
        width = right  - left 
        min_height = min(height[left],  height[right])
        area = min_height * width 

        max_water = max(area, max_water) 

        # Move the pointer of the lowest number in each iteration 
        if height[left] <= height[right]:
            left += 1
        else: # Right pointer is the smallest this iteration 
            right -= 1

    return max_water


###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestGroupAnagrams(unittest.TestCase):
    def test_one(self):
        height = [1,8,6,2,5,4,8,3,7]
        solution = 49
        self.assertEqual(maxArea(height), solution)

    def test_two(self):
        height = [1,1]
        solution = 1
        self.assertEqual(maxArea(height), solution)


if __name__ == "__main__":
    unittest.main() 
