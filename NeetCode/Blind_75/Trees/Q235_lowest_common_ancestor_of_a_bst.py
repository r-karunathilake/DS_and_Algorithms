""" Question 235: Lowest Common Ancestor of a Binary Search Tree

Description: Given a binary search tree (BST), find the lowest common ancestor 
             (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor 
is defined between two nodes p and q as the lowest node in T that has both p 
and q as descendants (where we allow a node to be a descendant of itself).”

Constraints:

    The number of nodes in the tree is in the range [2, 105].
            -109 <= Node.val <= 109
            All Node.val are unique.
            p != q
            p and q will exist in the BST.

    Time Complexity:  O(N)
    Space Complexity: O(N)

Where N is the number of nodes in the tree. 
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is None:
        return None
    
    # If both nodes are smaller than the root, check the left sub-tree
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    
    # If both nodes are larger than the root, check the right sub-tree
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)

    # If 'p' and 'q' are on either side of the root 
    #                 or 
    # Either 'p' or 'q' is the root node
    return root

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestLowestCommonAncestor(unittest.TestCase):
    def test_one(self):
        #       6
        #     /   \
        #    /     \
        #   2       8
        #  / \     / \
        # 0   4   7   9
        #    / \
        #   3   5
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)

        p = TreeNode(7)
        q = TreeNode(9)

        solution = 8

        self.assertEqual(lowestCommonAncestor(root, p, q).val, solution)

    def test_two(self):
        #       6
        #     /   \
        #    /     \
        #   2       8
        #  / \     / \
        # 0   4   7   9
        #    / \
        #   3   5
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)

        p = TreeNode(2)
        q = TreeNode(4)

        solution = 2

        self.assertEqual(lowestCommonAncestor(root, p, q).val, solution)

if __name__ == "__main__":
    unittest.main() 
