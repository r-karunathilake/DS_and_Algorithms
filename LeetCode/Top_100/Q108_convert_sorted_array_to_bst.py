""" Question 108: Convert Sorted Array to Binary Search Tree

Description: Given an integer array nums where the elements are sorted in 
             ascending order, convert it to a height-balanced binary search tree.

Constraints:
               1 <= nums.length <= 10^4
           -10^4 <= nums[i]     <= 10^4
        

nums is sorted in a strictly increasing order.
"""
from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: list[int]) -> Optional[TreeNode]:
    if not nums:
        return None
            
    m = len(nums) // 2
    root = TreeNode(nums[m])
    root.left = sortedArrayToBST(nums[: m])
    root.right = sortedArrayToBST(nums[m + 1:])

    return root

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestBST(unittest.TestCase):
    @staticmethod
    def inorderTraverse(root: TreeNode) -> list[int]:
        if not root:
            return []
        
        stack = []
        result = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left 

            root = stack.pop()
            result.append(root.val)

            root = root.right 

        return result 

    def test_one(self):
        nums = [-10,-3,0,5,9]
        self.assertEqual(TestBST.inorderTraverse(sortedArrayToBST(nums)), 
                         [-10, -3, 0, 5, 9])

    def test_two(self):
        nums = [1,3]
        self.assertEqual(TestBST.inorderTraverse(sortedArrayToBST(nums)), 
                         [1,3])

if __name__ == "__main__":
    unittest.main() 
