""" Question 104: Maximum Depth of Binary Tree

Description: Given the root of a binary tree, return its maximum depth. A binary 
             tree's maximum depth is the number of nodes along the longest path 
             from the root node down to the farthest leaf node.

Constraints:
                 0 <= number of nodes <= 10^4
              -100 <= Node.val        <= 100
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepthRecursive(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    l_depth = maxDepthRecursive(root.left)
    r_depth = maxDepthRecursive(root.right)

    return max(l_depth, r_depth) + 1    

# Iterative solution
from collections import deque 

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    while queue:
        current_node, level = queue.popleft()
        if current_node.right:
            queue.append((current_node.right, level + 1))
        if current_node.left:
            queue.append((current_node.left, level + 1))
        
    return level 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestMaxDepth(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(maxDepth(None), 0)

    def test_one_node(self):
        self.assertEqual(maxDepth(TreeNode(2)), 1)

    def test_small_tree(self):
        # 1
        #  \
        #   2
        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(maxDepth(root), 2)

    def test_large_tree(self):
        #           3
        #          / \
        #         9   20
        #             / \
        #            15  7 
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(maxDepth(root), 3)

if __name__ == "__main__":
    unittest.main() 
