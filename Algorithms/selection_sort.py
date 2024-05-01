""" Sort an array of numbers in ascending order. 

Time Complexity: O(N^2)
Space Complexity: O(1)

Where N is the number of elements in the array to be sorted. 
"""

def selection_sort(arr: list) -> None:
    length = len(arr)
    for current_idx in range(length):
        for search_idx in range(current_idx + 1, length):
            if arr[current_idx] > arr[search_idx]:
                arr[current_idx], arr[search_idx] = arr[search_idx], arr[current_idx]

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestSS(unittest.TestCase):
    def test_one(self):
        nums  = [1, 2, 5, 6, 4, 0]
        solution = [0, 1, 2, 4, 5, 6]
        selection_sort(nums)
        self.assertEqual(nums, solution)
    
    def test_two(self):
        nums  = [-2, 45, 0, 11, -9,88,-97,-202,747]
        solution = [-202, -97, -9, -2, 0, 11, 45, 88, 747]
        selection_sort(nums)
        self.assertEqual(nums, solution)

if __name__ == "__main__":
    unittest.main()
