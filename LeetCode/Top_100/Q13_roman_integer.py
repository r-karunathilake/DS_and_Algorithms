""" Question 13: Roman to Integer

Description: 
Roman numerals are represented by seven different symbols: 
I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as 
XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written 
as IV. Because the one is before the five we subtract it making four. The same 
principle applies to the number nine, which is written as IX. There are six 
instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
Constraints:
               1 <= s.length <= 15
               s[i] is a set of {"I", "V", "X", "L", "C", "D", "M"}

Note: It is guaranteed that 's' is a valid roman numeral in the range [1, 3999] 
"""

"""First solution using built-in functions
   Time Complexity:  O(N)
   Space Complexity: O(1)

   Where N is the number of characters in the string 
"""
def romanToInt(string: str) -> int:
    sum = 0
    length = len(string)
    romanMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for idx, char in enumerate(string):
        value = romanMap[char]
        if idx < length - 1 and value < romanMap[string[idx + 1]]:
            sum -= value
        else: 
            sum += value
    return sum 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestRomanInteger(unittest.TestCase):
    def test_one(self):
        s = "I"
        self.assertEqual(romanToInt(s), 1)

    def test_three(self):
        s = "III"
        self.assertEqual(romanToInt(s), 3)
    
    def test_four(self):
        s = "IV"
        self.assertEqual(romanToInt(s), 4)

    def test_four(self):
        s = "MCMXCIV"
        self.assertEqual(romanToInt(s), 1994)

if __name__ == "__main__":
    unittest.main() 
