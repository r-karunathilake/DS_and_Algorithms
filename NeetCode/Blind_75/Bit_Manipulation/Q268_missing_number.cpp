/* Question 268: Missing Number

Description: Given an array nums containing n distinct numbers in the range 
             [0, n], return the only number in the range that is missing from 
             the array.

Constraints:
                
                n == nums.length
                1 <= n <= 104
                0 <= nums[i] <= n
                All the numbers of nums are unique.

*/
#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    int missingNumber(std::vector<int>& nums) {
        int n {static_cast<int>(nums.size())};
        /* equals n b/c we need to add the last element. 
        For loop only goes till n - 1*/
        int result {n}; 
        for(int i {0}; i < n; ++i){
            result ^= i ^ nums[i];
        }
        return result;
    }
};

/*##############################################################################
###############                  TEST CASES                     ###############
###############################################################################*/
int main() {
    Solution solution;

    // Test cases
    std::vector<int> nums1 = {3, 0, 1};
    assert(solution.missingNumber(nums1) == 2);

    std::vector<int> nums2 = {0, 1};
    assert(solution.missingNumber(nums2) == 2);

    std::vector<int> nums3 = {9,6,4,2,3,5,7,0,1};
    assert(solution.missingNumber(nums3) == 8);

    std::vector<int> nums4 = {0};
    assert(solution.missingNumber(nums4) == 1);

    std::cout << "All test cases passed!" << std::endl;

    return 0;
}
