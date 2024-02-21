""" Question 226: Invert Binary Tree

Description: Given the root of a binary tree, invert the tree, and return its 
             root.

Constraints:
                 0 <= number of nodes <= 100
              -100 <= Node.val        <= 100
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTreeRecursive(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Empty tree
    if not root:
        return None  

    # Swap the children 
    root.left, root.right = root.right, root.left 
    
    invertTreeRecursive(root.left)
    invertTreeRecursive(root.right)

    return root

# Iterative solution
from collections import deque 

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    queue = deque([root])

    while queue:
        current_root = queue.popleft()

        # Swap the children 
        current_root.left, current_root.right = current_root.right, current_root.left 

        if current_root.left:
            queue.append(current_root.left)
        if current_root.right:
            queue.append(current_root.right)
        
    return root 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestMaxDepth(unittest.TestCase):
    def inorderTraversal(self, root: Optional[TreeNode], result: list) -> List[int]:
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.val)
            self.inorderTraversal(root.right, result)

    def test_empty_tree(self):
        self.assertEqual(invertTree(None), None)

    def test_one_node(self):
        answer = []
        self.inorderTraversal(invertTree(TreeNode(2)), answer)
        self.assertEqual(answer, [2])

    def test_small_asymmetric_tree(self):
        # 1        1
        #  \  ->  /
        #   2    2
        root = TreeNode(1, None, TreeNode(2))
        answer = []
        self.inorderTraversal(invertTree(root), answer)
        self.assertEqual(answer, [2, 1])

    def test_small_tree(self):
        #     1           1
        #    / \    ->   / \
        #   3   2       2   3 
        root = TreeNode(1, TreeNode(3), TreeNode(2))
        answer = []
        self.inorderTraversal(invertTree(root), answer)
        self.assertEqual(answer, [2, 1, 3])

    def test_large_tree(self):
        #           3              3
        #          / \            / \
        #         9   20   ->    20  9
        #             / \       / \
        #            15  7     7   15 
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        answer = []
        self.inorderTraversal(invertTree(root), answer)
        self.assertEqual(answer, [7, 20, 15, 3, 9])

if __name__ == "__main__":
    unittest.main() 
