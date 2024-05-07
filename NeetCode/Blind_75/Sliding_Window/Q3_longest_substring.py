""" Question 3: Longest Substring Without Repeating Characters

Description: Given a string s, find the length of the longest
             substring without repeating characters.


Note : s consists of English letters, digits, symbols and spaces.

Constraints:
               2 <= s.length <= 5 * 10^4
           
   Time complexity: O(N)
   Space complexity: O(N)

   Where N in the number of characters in the string
"""

def lengthOfLongestSubstring(s: str) -> int:
    # Sliding window method
    characters = set() 
    max_length = 0

    l_ptr = 0
    for r_ptr in range(len(s)): 
        # End of this substring
        while s[r_ptr] in characters:
            characters.remove(s[l_ptr])
            l_ptr += 1
            
        characters.add(s[r_ptr])
        max_length = max(max_length, r_ptr - l_ptr + 1)

    return max_length


###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestGroupAnagrams(unittest.TestCase):
    def test_one(self):
        height = "abcabcbb"
        solution = 3
        self.assertEqual(lengthOfLongestSubstring(height), solution)

    def test_two(self):
        height = "pwwkew"
        solution = 3
        self.assertEqual(lengthOfLongestSubstring(height), solution)
  
    def test_three(self):
        height = " "
        solution = 1
        self.assertEqual(lengthOfLongestSubstring(height), solution)


if __name__ == "__main__":
    unittest.main() 
