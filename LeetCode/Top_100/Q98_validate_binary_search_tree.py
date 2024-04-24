""" Question 98: Validate Binary Search Tree

Description: Given the 'root' of a binary tree, determine if it is a 
             valid binary search tree (BST).

             A valid BST is defined as follows:
                - The left subtree of a node contains only nodes with keys less than the node's key.
                - The right subtree of a node contains only nodes with keys greater than the node's key. 
                - Both the left and right subtrees must also be binary search trees. 

Constraints:
                 1 <= Number of Nodes <= 10^4
             -2^32 <= Node.val        <= 2^31 - 1 
"""

from typing import Optional, List

"""The big O of this solution is as follows:
    
   Time complexity: O(N)
   Space complexity: O(N) -> Stack space used due to recursive call  

   Where N is the number of nodes in the BST. 
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode], current_min = float("-inf"), current_max = float("inf")) -> int:
    # Base case 
    if not root:
        return True 

    # Check if current node is in the valid range of values 
    if not (current_min < root.val < current_max):
        return False

    # Recursively check the rest of the tree
    return (isValidBST(root.left, current_min, root.val) and isValidBST(root.right, root.val, current_max))
            

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestIsValidBST(unittest.TestCase):
    def test_valid_small_tree(self):
        """
                2
               / \
              1   3         
        """
        root_node = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(isValidBST(root_node), True)
    
    def test_invalid_small_tree(self):
        """
                    5
                   / \
                  1   \
                       4
                      / \ 
                     3   6 
        """
        root_node = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        self.assertEqual(isValidBST(root_node), False)
    
    def test_valid_large_tree(self):
        """
                8
               / \
              /   \
             6     99
            / \   / \
           0   7 80 100 
        """
        root_node = TreeNode(8, TreeNode(6, TreeNode(0), TreeNode(7)), TreeNode(99, TreeNode(80), TreeNode(100)))
        self.assertEqual(isValidBST(root_node), True)

    def test_invalid_large_tree(self):
        """
                8
               / \
              /   \
             1     9
            / \   / \
          -1   2 6   10 
        """
        root_node = TreeNode(8, TreeNode(1, TreeNode(-1), TreeNode(2)), TreeNode(9, TreeNode(6), TreeNode(10)))
        self.assertEqual(isValidBST(root_node), False)

if __name__ == '__main__':
    unittest.main()
