""" Question 572: Subtree of Another Tree

Description: Given the roots of two binary trees root and subRoot, return true 
             if there is a subtree of root with the same structure and node 
             values of subRoot and false otherwise.

            A subtree of a binary tree tree is a tree that consists of a node 
            in tree and all of this node's descendants. The tree tree could 
            also be considered as a subtree of itself.

Constraints:


    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].

                    -104 <= root.val    <= 104
                    -104 <= subRoot.val <= 104


    Time Complexity:  O(N x M)
    Space Complexity: O(N + M)

Where N is the number of nodes in the 'root' tree and M is the number of nodes
in 'subRoot'.
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


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # Base Case
    if not root:
        return False

    if isSameTree(root, subRoot):
        return True 
    
    # Otherwise, recursively search down the 'root' tree for the 'subTree'
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot) 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestRotatedMin(unittest.TestCase):
    def test_true(self):
        #     3
        #    / \
        #   4   5
        #  / \
        # 1   2
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.right = TreeNode(5)

        #    4
        #   / \
        #  1   2
        subTree = TreeNode(4)
        subTree.left = TreeNode(1)
        subTree.right = TreeNode(2)

        self.assertTrue(isSubtree(root, subTree))
    
    def test_false(self):
        #     3
        #    / \
        #   4   5
        #  / \
        # 1   2
        #    /
        #   0 
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(0)
        root.right = TreeNode(5)

        #    4
        #   / \
        #  1   2
        subTree = TreeNode(4)
        subTree.left = TreeNode(1)
        subTree.right = TreeNode(2)

        self.assertFalse(isSubtree(root, subTree))

if __name__ == "__main__":
    unittest.main() 
