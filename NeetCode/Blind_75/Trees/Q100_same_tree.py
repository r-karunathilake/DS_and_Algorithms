""" Question 100: Same Tree

Description: Given the roots of two binary trees p and q, write a 
             function to check if they are the same or not. Two binary 
             trees are considered the same if they are structurally identical, 
             and the nodes have the same value.

Constraints:

    The number of nodes in both trees is in the range [0, 100].
                
                -104 <= Node.val <= 104

    Time Complexity:  O(N)
    Space Complexity: O(1)

Where N is the total number of nodes in the trees
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True 
    
    if not p or not q:
        return False 
    
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestRotatedMin(unittest.TestCase):

    def test_true(self):
        #    1
        #   / \
        #  2   3
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        #    1
        #   / \
        #  2   3
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)

        self.assertTrue(isSameTree(p, q))
    
    def test_false(self):
        #    1
        #   / 
        #  2   
        p = TreeNode(1)
        p.left = TreeNode(2)

        #  1
        #   \
        #    2
        q = TreeNode(1)
        q.right = TreeNode(2)
        self.assertFalse(isSameTree(p, q))
    
    def test_true_two(self):
        #    5
        #   / \
        #  1   4
        #     / \
        #    3   6
        p = TreeNode(5)
        p.left = TreeNode(1)
        p.right = TreeNode(4)
        p.right.left = TreeNode(3)
        p.right.right = TreeNode(6)

        #    5
        #   / \
        #  1   4
        #     / \
        #    3   6
        q = TreeNode(5)
        q.left = TreeNode(1)
        q.right = TreeNode(4)
        q.right.left = TreeNode(3)
        q.right.right = TreeNode(6)

        self.assertTrue(isSameTree(p, q))
if __name__ == "__main__":
    unittest.main() 
