/* Question 191: Number of 1 Bits 

Description: Write a function that takes the binary representation of a positive integer and returns the number of
             set bits it has (also known as the Hamming weight).

Constraints:    
                   1 <= n <= 2^31 - 1
*/

#include <iostream>
#include <cassert>

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count {};
        while(n){
            count += n & 1; // Check if the last bit is set (n & 1 = 1 or 0)
            n >>= 1; // Done processing the last bit 
        }
        return count;
    }
};

/*##############################################################################
###############                  TEST CASES                     ###############
###############################################################################*/

int main() {
    Solution solution;

    // Test cases
    assert(solution.hammingWeight(0b00000000000000000000000000001011) == 3);
    assert(solution.hammingWeight(0b00000000000000000000000010000000) == 1);
    assert(solution.hammingWeight(0b11111111111111111111111111111101) == 31);
    assert(solution.hammingWeight(0b00000000000000000000000000000000) == 0);
    assert(solution.hammingWeight(0b11111111111111111111111111111111) == 32);

    std::cout << "All test cases passed!" << std::endl;

    return 0;
}
