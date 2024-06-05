/* Question 27: Merge Sorted Array  

Description: Given an integer array nums and an integer val, remove all 
             occurrences of val in nums in-place. The order of the elements 
             may be changed. Then return the number of elements in nums which 
             are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to 
get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the 
elements which are not equal to val. The remaining elements of nums are not 
important as well as the size of nums.

Return k.

Constraints:
    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100
*/
#include <vector>
#include <utility>
#include <iostream>
#include <cassert>

class Solution {
public:
    auto removeElement(std::vector<int>& nums, int val) -> int{  
        size_t k {};
        for(size_t i {}; i < nums.size(); ++i){
            if(nums[i] != val){
                nums[k] = nums[i];
                ++k;
            }
        }
        return k;
    }
};

/*##############################################################################
###############                  TEST CASES                     ###############
###############################################################################*/
void testRemoveElement() {
    Solution* sol {new Solution()};
    {
        std::vector<int> nums = {3, 2, 2, 3};
        int val = 3;
        int new_length = sol->removeElement(nums, val);
        std::vector<int> expected = {2, 2}; // First 'new_length' elements
        assert(new_length == expected.size());
        assert(std::vector<int>(nums.begin(), nums.begin() + new_length) == expected);
    }
    {
        std::vector<int> nums = {0, 1, 2, 2, 3, 0, 4, 2};
        int val = 2;
        int new_length =  sol->removeElement(nums, val);
        std::vector<int> expected = {0, 1, 3, 0, 4}; // First 'new_length' elements
        assert(new_length == expected.size());
        assert(std::vector<int>(nums.begin(), nums.begin() + new_length) == expected);
    }
    {
        std::vector<int> nums = {1};
        int val = 1;
        int new_length =  sol->removeElement(nums, val);
        std::vector<int> expected = {}; // First 'new_length' elements
        assert(new_length == expected.size());
        assert(std::vector<int>(nums.begin(), nums.begin() + new_length) == expected);
    }
    {
        std::vector<int> nums = {1, 2, 3, 4, 5};
        int val = 6;
        int new_length =  sol->removeElement(nums, val);
        std::vector<int> expected = {1, 2, 3, 4, 5}; // First 'new_length' elements
        assert(new_length == expected.size());
        assert(std::vector<int>(nums.begin(), nums.begin() + new_length) == expected);
    }
    {
        std::vector<int> nums = {2, 2, 2, 2};
        int val = 2;
        int new_length =  sol->removeElement(nums, val);
        std::vector<int> expected = {}; // First 'new_length' elements
        assert(new_length == expected.size());
        assert(std::vector<int>(nums.begin(), nums.begin() + new_length) == expected);
    }

    std::cout << "All test cases passed!\n";
    delete sol; 
}

int main() {
    testRemoveElement();
    return 0;
}
