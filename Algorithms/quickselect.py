""" This quickselect alogorithm is a combination of quick sort and 
binary search.Additionally, we an find the value we are looking for without 
sorting the entire array! 

Best and Average Time Complexity: O(N)
Worst Time Complexity: O(N^2)  <---- poor array partitioning 

=====b/c Recursive call on the stack===== 
Best and Average Space Complexity: O(logN)
Worst Space Complexity: O(N) <---- poor array partitioning 
"""
from quicksort import partition 
def quickselect(nums: list[int], kth_lowest_val_idx: int, 
                left_ptr: int, right_ptr: int) -> int:
    # Base case 
    if right_ptr - left_ptr <= 0:
        return nums[left_ptr]
    
    # Partition the 'nums' array and grab the pivot index 
    pivot_idx = partition(nums, left_ptr, right_ptr)

    # If the target value index left of pivot index
    if kth_lowest_val_idx < pivot_idx:
        # Recursively perform quickselect on the left sub-array
        return quickselect(nums, kth_lowest_val_idx, left_ptr, pivot_idx - 1)
    # If the target value index right of pivot index
    elif kth_lowest_val_idx > pivot_idx:
        # Recursively perform quickselect on the right sub-array
        return quickselect(nums, kth_lowest_val_idx, pivot_idx + 1, right_ptr)
    else: # kth_lowest_val_idx == pivot_idx 
        return nums[pivot_idx]

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestQS(unittest.TestCase):
    def test_one(self):
        nums  = [0, -1, 2, 3, -4, 5, 7]
        solution = -4
        search_start = 0
        search_end = len(nums) - 1
        select_lowest_number = 0
        self.assertEqual(quickselect(nums, select_lowest_number, search_start, search_end), solution)

    def test_two(self):
        nums  = [-99, -50, 0, 33, -1, 50, 725]
        solution = 0
        search_start = 0
        search_end = len(nums) - 1
        select_4th_lowest_number = 3
        self.assertEqual(quickselect(nums, select_4th_lowest_number, search_start, search_end), solution)

if __name__ == "__main__":
    unittest.main() 
