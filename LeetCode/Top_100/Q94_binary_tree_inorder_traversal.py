""" Question 94: Binary Tree InOrder Traversal 

Description: Given the root of a binary tree, return the inorder traversal of its 
             nodes' values. 

Constraints:
                 0 <= number of nodes <= 100
              -100 <= node.val        <= 100

Note: complete both recursively and iteratively. 
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    traverseRecursive(root, result)
    return result

def traverseRecursive(root: Optional[TreeNode], ans: List[int]):
    if root:
        traverseRecursive(root.left, ans)
        ans.append(root.val)
        traverseRecursive(root.right, ans)

def traverseIteratively(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    
    while root or stack:
        # Navigate down the left sub-branch of the tree if it exists 
        while root:
            stack.append(root)
            root = root.left 
        
        # 'root' is now left-most node of the sub-branch 
        root = stack.pop()
        result.append(root.val)
        # Make sure to go down the right sub-branch if it exists
        root = root.right
        
    return result

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestTreeTraversal(unittest.TestCase):
    def test_empty_root(self):
        root = None
        self.assertEqual(inorderTraversal(root), [])
        self.assertEqual(traverseIteratively(root), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(inorderTraversal(root), [1])
        self.assertEqual(traverseIteratively(root), [1])

    def test_three_nodes(self):
        #    1
        #   / \
        #  2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertEqual(inorderTraversal(root), [2, 1, 3])
        self.assertEqual(traverseIteratively(root), [2, 1, 3])
    
    def test_five_nodes(self):
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

        self.assertEqual(inorderTraversal(root), [1, 5, 3, 4, 6])
        self.assertEqual(traverseIteratively(root), [1, 5, 3, 4, 6])

if __name__ == '__main__':
    unittest.main()
