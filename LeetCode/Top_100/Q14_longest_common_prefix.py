""" Question 14: Longest Common Prefix

Description: Write a function to find the longest common prefix string 
             amongst an array of strings.

Constraints:
               1 <= strs.length    <= 200
               0 <= strs[i].length <= 200

Note: strs[i] is only lowercase English letters 
"""
from typing import List

"""First solution using built-in functions
   Time Complexity:  O(N * M + K) 
   Space Complexity: O(N * M)

   Where N is the number of string in the input list and M is
   the average length of the strings, and K is the length of the 
   shortest string. 
"""
def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""
    letter_groups = zip(*strs)

    for group in letter_groups:
        # If the letters in the 'group' are NOT all the same
        if len(set(group)) > 1:
            break
        prefix += group[0]

    return prefix

"""A second solution without using built-in functions
   Time Complexity:  O(N * M) 
   Space Complexity: O(1)

   Where N is the number of string in the input list and M is
   the length of the longest string. 
"""
def longestPrefix(strs: List[str]) -> str:
    # Only one string, thus it is the longest prefix 
    if len(strs) == 1:
        return strs[0]

    # Assume the prefix is the first string in the array
    prefix = strs[0]
    # Maximum prefix length is the length of the first string at this point in 
    # the algorithm
    max_prefix_len = len(prefix)  

    # Loop through the second string on, if it exists... 
    for string in strs[1::]:
        while prefix != string[:max_prefix_len]:
            # The prefix must have atleast one less character
            max_prefix_len -= 1
            prefix = prefix[:max_prefix_len]

        # If the prefix length becomes zero after a full string evaluation
        # we have a empty prefix by definition. 
        if max_prefix_len == 0:
            return ""
        
    return prefix

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestLongestPrefix(unittest.TestCase):
    def test_empty_prefix(self):
        strs = ["dog", "racecar", "car"]
        self.assertEqual(longestCommonPrefix(strs), "")
        self.assertEqual(longestPrefix(strs), "")

    def test_prefix(self):
        strs = ["flower", "flow", "flight"]
        self.assertEqual(longestCommonPrefix(strs), "fl")
        self.assertEqual(longestPrefix(strs), "fl")

if __name__ == "__main__":
    unittest.main() 
