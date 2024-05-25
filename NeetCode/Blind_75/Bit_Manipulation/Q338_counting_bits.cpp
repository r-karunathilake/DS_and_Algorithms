/* Question 338: Counting Bits

Description: Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the 
             number of 1's in the binary representation of i.

Constraints:    
                    0 <= n <= 105
*/

#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    std::vector<int> countBits(int n) {
        // Keep track of results for 
        // dynamic programming memoization 
        std::vector<int> result(n + 1, 0);

        for(int i {1}; i <= n; ++i){
            //                i / 2      i % 2 (get the last bit)
            result[i] = result[i >> 1] + (i & 1);
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
    std::vector<int> result1 = solution.countBits(2);
    assert(result1 == std::vector<int>({0, 1, 1}));

    std::vector<int> result2 = solution.countBits(5);
    assert(result2 == std::vector<int>({0, 1, 1, 2, 1, 2}));

    std::vector<int> result3 = solution.countBits(0);
    assert(result3 == std::vector<int>({0}));

    std::vector<int> result4 = solution.countBits(1);
    assert(result4 == std::vector<int>({0, 1}));

    std::vector<int> result5 = solution.countBits(10);
    assert(result5 == std::vector<int>({0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2}));

    std::cout << "All test cases passed!" << std::endl;

    return 0;
}
