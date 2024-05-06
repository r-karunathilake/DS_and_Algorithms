""" Question 125: Valid Palindrome

Description: A phrase is a palindrome if, after converting all uppercase 
             letters into lowercase letters and removing all non-alphanumeric 
             characters, it reads the same forward and backward. Alphanumeric 
             characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Constraints:
               1 <= s.length <= 2 * 10^5

Note: s consists only of printable ASCII characters.
"""


""" 
   Time complexity: 
   Space complexity: 
"""
def isPalindrome(string: str) -> bool:
    string = string.lower()

    left = 0
    right = len(string) - 1

    while left <= right:
        
        if not string[left].isalnum():
            left += 1
            continue 

        if not string[right].isalnum():
            right -= 1
            continue 

        # Valid character found 
        if string[left] != string[right]:
            return False 

        left += 1
        right -= 1
    return True 
    
###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestGroupAnagrams(unittest.TestCase):
    def test_true(self):
        string = "A man, a plan, a canal: Panama"
        self.assertEqual(isPalindrome(string), True)

    def test_false(self):
        string = "race a car"
        self.assertEqual(isPalindrome(string), False)

    def test_empty(self):
        string = ""
        self.assertEqual(isPalindrome(string), True)

if __name__ == "__main__":
    unittest.main() 
