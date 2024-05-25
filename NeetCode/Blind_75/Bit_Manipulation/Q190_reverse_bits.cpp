/* Question 190: Reverse Bits

Description: Reverse bits of a given 32 bits unsigned integer.

Constraints:
                
                The input must be a binary string of length 32

Follow up: If this function is called many times, how would you optimize it?

*/
#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result {};
        for(int i {}; i < 32; ++i){
            result <<= 1; // Shift result to the left to make room for the next bit
            result |= n & 1; // Get the last bit of n and add it to result
            n >>= 1; // Shift n to the right to process the next bit
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
    assert(solution.reverseBits(0b00000010100101000001111010011100) == 0b00111001011110000010100101000000);
    assert(solution.reverseBits(0b11111111111111111111111111111101) == 0b10111111111111111111111111111111);
    assert(solution.reverseBits(0b00000000000000000000000000000000) == 0b00000000000000000000000000000000);
    assert(solution.reverseBits(0b10000000000000000000000000000000) == 0b00000000000000000000000000000001);
    assert(solution.reverseBits(0b11111111111111110000000000000000) == 0b00000000000000001111111111111111);

    std::cout << "All test cases passed!" << std::endl;

    return 0;
}
