""" Question 20: Valid Parentheses

Description: Given a string s containing just the characters 
             '(', ')', '{', '}', '[' and ']', determine 
             if the input string is valid.

An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
 

Constraints:
               1 <= s.length <= 10^4

Note: 's' consists of parentheses only '()[]{}'
"""

def isValid(s: str) -> bool:
    if len(s) <= 1:
        return False 

    stack = []
    map = {"(": ")", "[": "]", "{": "}"}
    for char in s:
        # Found an opening bracket
        if char in map.keys():
            stack.append(char)
            continue

        # A closing bracket found 
        if not stack or map[stack.pop()] != char:
            return False 
    
    # If the stack is not empty 
    if stack:
        return False
    return True 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestPermutation(unittest.TestCase):
    def test_one(self):
        string = "()"
        self.assertTrue(isValid(string))

    def test_two(self):
        string = "()[]{}"
        self.assertTrue(isValid(string))

    def test_three(self):
        string = "(}"
        self.assertFalse(isValid(string))

    def test_four(self):
        string = "()[(){}]{}"
        self.assertTrue(isValid(string))

    def test_five(self):
        string = "([()[}])"
        self.assertFalse(isValid(string))
    
    def test_six(self):
        string = "("
        self.assertFalse(isValid(string))
    
    def test_seven(self):
        string = "(("
        self.assertFalse(isValid(string))

if __name__ == "__main__":
    unittest.main() 
