/* Question 88: Merge Sorted Array  

Description: You are given two integer arrays nums1 and nums2, sorted in 
             non-decreasing order, and two integers m and n, representing the 
             number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be 
stored inside the array nums1. To accommodate this, nums1 has a length of 
m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length 
of n.

Constraints:
        nums1.length == m + n
        nums2.length == n
        0 <= m, n <= 200
        1 <= m + n <= 200
        -10^9 <= nums1[i], nums2[j] <= 10^9
*/

#include <vector>
#include <cassert>
#include <iostream>

class Solution{
    public:
        auto merge(std::vector<int>& nums1, int m, 
                   std::vector<int>& nums2, int n) -> void{

            // Signed integer 
            m = static_cast<ssize_t>(m);
            n = static_cast<ssize_t>(n);

            while(m > 0 && n > 0){
                if(nums1[m - 1] > nums2[n-1]){
                    nums1[m + n - 1] = nums1[m - 1];
                    --m; 
                }
                else{ // num1 value <= to num2 value 
                    nums1[m + n - 1] = nums2[n - 1];
                    --n;  
                }
            }

            /* If m was < n, then we have left over nums2 values to append to
            the end of nums1 */
            while(n > 0){
                nums1[m + n - 1] = nums2[n - 1];
                --n;
            }
        }
};


/*##############################################################################
###############                  TEST CASES                     ###############
###############################################################################*/
void testMerge() {
    Solution sol;
    {
        std::vector<int> nums1 = {1, 2, 3, 0, 0, 0};
        std::vector<int> nums2 = {2, 5, 6};
        sol.merge(nums1, 3, nums2, 3);
        std::vector<int> expected = {1, 2, 2, 3, 5, 6};
        assert(nums1 == expected);
    }
    {
        std::vector<int> nums1 = {1, 2, 3, 0, 0, 0};
        std::vector<int> nums2 = {4, 5, 6};
        sol.merge(nums1, 3, nums2, 3);
        std::vector<int> expected = {1, 2, 3, 4, 5, 6};
        assert(nums1 == expected);
    }
    {
        std::vector<int> nums1 = {4, 5, 6, 0, 0, 0};
        std::vector<int> nums2 = {1, 2, 3};
        sol.merge(nums1, 3, nums2, 3);
        std::vector<int> expected = {1, 2, 3, 4, 5, 6};
        assert(nums1 == expected);
    }
    {
        std::vector<int> nums1 = {0};
        std::vector<int> nums2 = {1};
        sol.merge(nums1, 0, nums2, 1);
        std::vector<int> expected = {1};
        assert(nums1 == expected);
    }
    {
        std::vector<int> nums1 = {1};
        std::vector<int> nums2 = {};
        sol.merge(nums1, 1, nums2, 0);
        std::vector<int> expected = {1};
        assert(nums1 == expected);
    }

    std::cout << "All test cases passed!\n";
}

int main() {
    testMerge();
    return 0;
}
