"""
Worst-Case Time Complexity: O(N^2)
Average Time Complexity: O(N * logN)
Best-Case Time Complexity: O(N * logN)

=====b/c Recursive call on the stack===== 
Worst Space Complexity: O(N) 
Average Time Complexity:  O(LogN)
Best Space Complexity: O(LogN) 
"""
# Pivot selection is very important for this algorithm. Ideally, the pivot
# should land in the middle of the array after partitioning 

def quick_sort(nums: list[int]) -> list:
    # Base case
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]  

        less = [i for i in nums[1:] if i <= pivot]
        greater = [i for i in nums[1:] if i > pivot]
        
        return quick_sort(less) + [pivot] + quick_sort(greater)

def partition(nums: list[int], left_ptr: int, right_ptr: int) -> int:
    # Choose the right pointer as the pivot index
    pivot_idx = right_ptr

    # Save the pivot value
    pivot = nums[pivot_idx]

    # Start the right pointer immediately to the left of the pivot
    right_ptr -= 1

    while True:
        # Move the left pointer to the right as long as the value at the
        # left pointer is less than the pivot value. 
        while nums[left_ptr] < pivot:
            left_ptr += 1

        # Move the right pointer to the left as long as the value at the 
        # right pointer is greater than the pivot value. 
        while nums[right_ptr] > pivot:
            right_ptr -= 1

        # Both left and right pointers have now stopped moving 

        # Check if the left pointer has reached or gone beyond the right pointer
        if left_ptr >= right_ptr:
            # Break because we need to swap the pivot value with the value at left pointer
            break
        
        # If the left pointer is still less than the right pointer, swap values
        # at left and right pointers.
        nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]

        # Increment the left pointer for the next iteration 
        left_ptr += 1
    
    # Swap the pivot value with the left pointer value
    nums[left_ptr], nums[pivot_idx] = nums[pivot_idx], nums[left_ptr]

    # Now the left pointer points to the correct position of the pivot in the array
    return left_ptr

"""
Worst-Case Time Complexity: O(N^2)
Average Time Complexity: O(N * logN)
Best-Case Time Complexity: O(N * logN)

=====b/c Recursive call on the stack===== 
Worst Space Complexity: O(N) 
Average Time Complexity:  O(LogN)
Best Space Complexity: O(LogN) 
"""

def quick_sort_in_place(nums: list[int], left_index: int, right_index: int) -> None:
    # Base case ('nums' length 0 or 1)
    if right_index - left_index <= 0:
        return 
    
    # Partition the 'nums' array and return the pivot index 
    pivot_idx = partition(nums, left_index, right_index)

    # Recursive call on left sub-array 
    quick_sort_in_place(nums, left_index, pivot_idx - 1)

    # Recursive call on the right sub-array
    quick_sort_in_place(nums, pivot_idx + 1, right_index)

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestQS(unittest.TestCase):
    def test_one(self):
        nums  = [0, -1, 2, 3, -4, 5, 7]
        solution = [-4, -1, 0, 2, 3, 5, 7]
        
        self.assertEqual(quick_sort(nums), solution)

    def test_two(self):
        nums = [0, -1, 2, 3, -4, 5, 7]
        solution = [-4, -1, 0, 2, 3, 5, 7]
        quick_sort_in_place(nums, 0, len(nums)-1)
        self.assertEqual(nums, solution)

if __name__ == "__main__":
    unittest.main() 
