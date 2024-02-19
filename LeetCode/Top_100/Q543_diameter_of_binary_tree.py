""" Question 543: Diameter of Binary Tree

Description: Given the root of a binary tree, return the length of the diameter 
             of the tree. The diameter of a binary tree is the length of the 
             longest path between any two nodes in a tree. This path may or may 
             not pass through the root.The length of a path between two nodes 
             is represented by the number of edges between them.

Constraints:
               1 <= tree.length <= 10^4
            -100 <= node.value  <  100
"""
from typing import List, Optional
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = 0
    # If only root node
    if not root.left and not root.right:
        return diameter
    
    node_stack = [(root, False)] # (node, visited?)
    depth = {None: 0}
    while node_stack:
        node, visited = node_stack.pop()
        
        # Processing leaf nodes children (None)
        if not node:
            continue

        if visited:
            left_depth = depth[node.left]
            right_depth = depth[node.right]

            # Update the diameter 
            diameter = max(diameter, left_depth + right_depth)

            # Update the depth for the current node 
            depth[node] = 1 + max(left_depth, right_depth)
        
        # Got the left-most node in the tree first then right-most node 
        else: 
            # Push the node with visited
            node_stack.append((node, True))
            # Push right and left children with not visited 
            node_stack.append((node.right, False))
            node_stack.append((node.left, False))

    return diameter

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestListMerge(unittest.TestCase):
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(diameterOfBinaryTree(root), 0)
    
    def test_two_nodes(self):
        #   1
        #  /
        # 2
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(diameterOfBinaryTree(root), 1)

    def test_three_nodes(self):
        #    1
        #   / \
        #  2   3
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(diameterOfBinaryTree(root), 2)

    def test_five_nodes(self):
        #    5
        #   / \
        #  1   4
        #     / \
        #    3   6
        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        self.assertEqual(diameterOfBinaryTree(root), 3)

if __name__ == "__main__":
    unittest.main() 
