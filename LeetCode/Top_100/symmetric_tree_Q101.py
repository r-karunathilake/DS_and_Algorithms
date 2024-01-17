""" Question 101: Symmetric Tree

Description: Given the root of a binary tree, check whether 
             it is a mirror of itself (i.e., symmetric 
             around its center).

Constraints:
                 1 <= number of nodes <= 1000
              -100 <= node.val        <= 100

Note: complete both recursively and iteratively. 
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

def isSymmetric(root: Optional[TreeNode], checkIter: bool=False) -> bool:
    # Empty root
    if not root:
        return True

    if not checkIter:
        return checkSymmetryRecursive(root.left, root.right)
    
    return checkSymmetryIteratively(root.left, root.right)

def checkSymmetryRecursive(left: TreeNode, right: TreeNode) -> bool:
    if not left and not right:
        return True 

    # Asymmetry found 
    if not left or not right: 
        return False 

    # Check values 
    if left.val != right.val:
        return False 
    
    # Check for symmetry down the tree 
    #                    1 (root)
    #                   / \
    #                  /   \ 
    #                 /     \
    #         (left) 2       2 (right)
    #               / \     / \
    #              /   \   /   \ 
    # (left.left) 3     4 4     3 (right.right)
    #                    ^
    #                    | 
    #       (left.right) & (right.left)

    return checkSymmetryRecursive(left.right, right.left) and checkSymmetryRecursive(left.left, right.right)
 
from collections import deque 

def checkSymmetryIteratively(left: TreeNode, right: TreeNode) -> bool:
    d_queue = deque([(left, right)])

    while d_queue:
        left, right = d_queue.popleft()

        if not left and not right:
            continue 
        
        if not left or not right:
            return False
        
        if left.val != right.val:
            return False 

        # Add the left and right children to the double-ended queue 
        d_queue.append((left.right, right.left))
        d_queue.append((left.left, right.right))

    return True 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestTreeTraversal(unittest.TestCase):
    def test_empty_tree(self):
        root = None
        self.assertTrue(isSymmetric(root))
        self.assertTrue(isSymmetric(root, True))
    
    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(isSymmetric(root))
        self.assertTrue(isSymmetric(root, True))

    def test_asymmetric_tree(self):
        #    1
        #   / \
        #  2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertFalse(isSymmetric(root))
        self.assertFalse(isSymmetric(root, True))
    
    def test_large_asymmetric_tree(self):
        #    5
        #   / \
        #  1   4
        #     / \
        #    3   6
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)

        self.assertFalse(isSymmetric(root))
        self.assertFalse(isSymmetric(root, True))

    def test_large_symmetric_tree(self):
        #         1
        #        / \
        #       /   \
        #      2     2
        #     / \   / \
        #    4   3 3   4
        
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(3)

        self.assertTrue(isSymmetric(root))
        self.assertTrue(isSymmetric(root, True))
        
if __name__ == '__main__':
    unittest.main()
