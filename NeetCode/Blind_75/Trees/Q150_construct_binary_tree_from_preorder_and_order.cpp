 /* Question 150: Construct Binary Tree from Preorder and Inorder Traversal

Description: Given two integer arrays preorder and inorder where preorder is the 
             preorder traversal of a binary tree and inorder is the inorder 
             traversal of the same tree, construct and return the binary tree.

Constraints:

            1 <= preorder.length         <= 3000
        -3000 <= preorder[i], inorder[i] <= 3000

         - inorder.length == preorder.length
         - preorder and inorder consist of unique values.
         - Each value of inorder also appears in preorder.
         - preorder is guaranteed to be the preorder traversal of the tree.
         - inorder is guaranteed to be the inorder traversal of the tree.

*/

#include <vector>
#include <iostream>
#include <cassert>
#include <stdexcept>
 
std::vector<int> spliceVector(const std::vector<int>& vec, size_t start, size_t end) {
    if (start > end || end > vec.size()) {
        throw std::out_of_range("Invalid start or end index");
    }
    return std::vector<int>(vec.begin() + start, vec.begin() + end);
}

 class TreeNode {
    public:
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode() : val(0), left(nullptr), right(nullptr) {}
        TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
        TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

class Solution {
public:
    TreeNode* buildTree(std::vector<int>& preorder, std::vector<int>& inorder) {
        // Base Case
        if (preorder.empty() || inorder.empty()){
            return nullptr; 
        }

        // First element of 'preorder' is always the root value 
        TreeNode* root = new TreeNode(preorder[0]); 

        // Find the root index in 'inorder' 
        int root_idx {-1}; 
        for(size_t i {}; i < inorder.size(); ++i){
            if(inorder[i] == root->val){
                root_idx = static_cast<int>(i);
                break;
            }
        }

        if (root_idx == -1) {
            throw std::runtime_error("Invalid input: root not found in inorder sequence.");
        }

        std::vector<int> left_preorder = spliceVector(preorder, 1, 1 + root_idx);
        std::vector<int> left_inorder = spliceVector(inorder, 0, root_idx);
        root->left = buildTree(left_preorder, left_inorder);

        std::vector<int> right_preorder = spliceVector(preorder, 1 + root_idx, preorder.size());
        std::vector<int> right_inorder = spliceVector(inorder, root_idx + 1, inorder.size());
        root->right = buildTree(right_preorder, right_inorder);
        
        return root;
    }
};

/*##############################################################################
###############                  TEST CASES                     ###############
###############################################################################*/

void testBuildTree() {
    Solution sol;

    // Test case 1: Regular case
    std::vector<int> preorder1 = {3, 9, 20, 15, 7};
    std::vector<int> inorder1 = {9, 3, 15, 20, 7};
    TreeNode* root1 = sol.buildTree(preorder1, inorder1);

    // Expected tree structure:
    //     3
    //    / \
    //   9  20
    //      / \
    //     15  7
    assert(root1->val == 3);
    assert(root1->left->val == 9);
    assert(root1->right->val == 20);
    assert(root1->right->left->val == 15);
    assert(root1->right->right->val == 7);

    // Test case 2: Single node
    std::vector<int> preorder2 = {1};
    std::vector<int> inorder2 = {1};
    TreeNode* root2 = sol.buildTree(preorder2, inorder2);

    // Expected tree structure:
    //  1
    assert(root2->val == 1);
    assert(root2->left == nullptr);
    assert(root2->right == nullptr);

    // Test case 3: Left skewed tree
    std::vector<int> preorder3 = {3, 2, 1};
    std::vector<int> inorder3 = {1, 2, 3};
    TreeNode* root3 = sol.buildTree(preorder3, inorder3);

    // Expected tree structure:
    //    3
    //   /
    //  2
    // /
    //1
    assert(root3->val == 3);
    assert(root3->left->val == 2);
    assert(root3->left->left->val == 1);
    assert(root3->left->right == nullptr);
    assert(root3->right == nullptr);

    // Test case 4: Right skewed tree
    std::vector<int> preorder4 = {1, 2, 3};
    std::vector<int> inorder4 = {1, 2, 3};
    TreeNode* root4 = sol.buildTree(preorder4, inorder4);

    // Expected tree structure:
    // 1
    //  \
    //   2
    //    \
    //     3
    assert(root4->val == 1);
    assert(root4->right->val == 2);
    assert(root4->right->right->val == 3);
    assert(root4->left == nullptr);
    assert(root4->right->left == nullptr);

    // Free the allocated memory for the test cases (not fully shown here for simplicity)
    // In practice, you should write a function to delete the entire tree

    std::cout << "All test cases passed!" << std::endl;
}

int main() {
    testBuildTree();
    return 0;
}
