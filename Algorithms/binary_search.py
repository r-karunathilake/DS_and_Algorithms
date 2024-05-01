"""
Time Complexity: O(log(N))
Space Complexity: O(1)

Where N in the number of elements in the array. 
"""
from typing import Optional 

def binary_search(arr: list, target: int) -> Optional[int]:
    l_idx = 0
    u_idx = len(arr) - 1

    while l_idx <= u_idx:
        # Interger division 
        m_idx = (l_idx + u_idx) // 2
        guess = arr[m_idx]

        if guess == target:
            return m_idx
        elif guess > target: 
            u_idx = m_idx - 1 
        else:
            l_idx = m_idx + 1
        
    # Target was not found 
    return None

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestBS(unittest.TestCase):
    def test_one(self):
        nums  = [0, 1, 2, 3, 4, 5, 7]
        idx = 3
        self.assertEqual(binary_search(nums, 3), idx)

    def test_two(self):
        nums  = [-3, -2, 0, 2, 4, 5, 7]
        idx = 0
        self.assertEqual(binary_search(nums, -3), idx)

if __name__ == "__main__":
    unittest.main() 
