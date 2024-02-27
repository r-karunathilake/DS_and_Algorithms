""" Question 70: Climbing Stairs

Description: You are climbing a staircase. It takes n steps to reach the top.
             Each time you can either climb 1 or 2 steps. In how many distinct
             ways can you climb to the top?

Constraints:
               1 <= n <= 45
"""
from typing import Optional

"""First solution big O is as follows:
   Time Complexity:  O(N) 
   Space Complexity: O(1)

   Where N is total loop iterations for 3 to "n"
"""
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    
    # Track the number of way to climb each step
    steps = [0] * (n + 1)

    # Base cases 
    steps[1] = 1
    steps[2] = 2

    # Fill the array 
    for i in range(3, n + 1):
        steps[i] = steps[i - 1] + steps[i - 2]
    
    return steps[n]

"""Second solution big O is as follows:
   Time Complexity:  O(N) due to memoization, Otherwise O(2^N)
   Space Complexity: O(2N) -> O(N) (Hash map + recursive stack call)

   Where N is the total number of steps 
"""
def climbStairsRecursive(n: int, steps: dict={}) -> int:
    if n <= 2:
        return n
    
    # Check if the result is already calculated 
    if n in steps:
        return steps[n]
    
    steps[n] = climbStairsRecursive(n - 1, steps) + climbStairsRecursive(n - 2, steps)
    
    # Save the result 
    return steps[n] 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestListMerge(unittest.TestCase):
    def test_single_step(self):
        self.assertEqual(climbStairs(1), 1)
        self.assertEqual(climbStairsRecursive(1), 1)

    def test_two_steps(self):
        # 1. 1 step + 1 step
        # 2. 2 steps 
        self.assertEqual(climbStairs(2), 2)
        self.assertEqual(climbStairsRecursive(2), 2)

    def test_three_steps(self):
        # 1. 1 step + 1 step + 1 step
        # 2. 2 steps + 1 step
        # 3. 1 step + 2 steps
        self.assertEqual(climbStairs(3), 3)
        self.assertEqual(climbStairsRecursive(3), 3)
    
    def test_four_steps(self):
        # 1. 1 step + 1 step + 1 step + 1 step
        # 2. 2 steps + 2 steps 
        # 3. 1 step + 1 step + 2 steps
        # 4. 2 steps + 1 step + 1 step
        # 5. 1 step + 2 steps + 1 step
        self.assertEqual(climbStairs(4), 5)
        self.assertEqual(climbStairsRecursive(4), 5)
    
    def test_five_steps(self):
        # 1. 1 step + 1 step + 1 step + 1 step + 1 step
        # 2. 2 step + 2 step + 1 step
        # 3. 1 step + 2 step + 2 step
        # 4. 2 step + 1 step + 2 step
        # 5. 1 step + 1 step + 2 step + 1 step
        # 6. 1 step + 2 step + 1 step + 1 step
        # 7. 1 step + 1 step + 1 step + 2 step
        # 8. 2 step + 1 step + 1 step + 1 step 
        self.assertEqual(climbStairs(5), 8)
        self.assertEqual(climbStairsRecursive(5), 8)

if __name__ == "__main__":
    unittest.main() 
