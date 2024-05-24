/* Question 371: Sum of Two Integers

Description: Given two integers a and b, return the sum of the two integers 
             without using any arithmetic operators +, -, *.

Constraints:
                -1000 <= a, b <= 1000
*/
#include <cassert>
#include <iostream>
#include <climits>

class Solution{
    public:
        int getSum(int a, int b) const{
            while(b != 0){
                int sum {a ^ b}; // Sum without carry 
                int carry {(a & b) << 1};  // Calculate carry and shift left by one

                a = sum;
                b = carry; 
            }
            return a;
        }
};

/*##############################################################################
###############                  TEST CASES                     ###############
###############################################################################*/
int main() {
    Solution solution;

    // Test cases
    assert(solution.getSum(1, 2) == 3);
    assert(solution.getSum(-1, 1) == 0);
    assert(solution.getSum(0, 0) == 0);
    assert(solution.getSum(100, 200) == 300);
    assert(solution.getSum(-2, 3) == 1);
    assert(solution.getSum(-5, -3) == -8);
    assert(solution.getSum(INT_MAX, 0) == INT_MAX);
    assert(solution.getSum(INT_MIN, 0) == INT_MIN);
    assert(solution.getSum(12345, 67890) == 80235);
    assert(solution.getSum(-12345, -67890) == -80235);

    std::cout << "All test cases passed!" << std::endl;

    return 0;
}
