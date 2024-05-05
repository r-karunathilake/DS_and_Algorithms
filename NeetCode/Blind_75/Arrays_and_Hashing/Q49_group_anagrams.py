""" Question 49: Group Anagrams 

Description: Given an array of strings strs, group the anagrams together. 
             You can return the answer in any order. An Anagram is a word or
             phrase formed by rearranging the letters of a different word or 
             phrase, typically using all the original letters exactly once.

Constraints:
               1 <= strs.length    <= 10^4
               0 <= strs[i].length <= 100
           
Note: strs[i] is only lowercase English letters 
"""


"""
   Time complexity: O(N * KlogK)
   Space complexity: O(N * K)

   Where N in the number of strings and K is the maximum length of a string.
"""
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # 'strs' with less than 1 strings (inclusive)
    if len(strs) <= 1:
        return [strs]

    result = {}
    for str in strs:
        sorted_str = "".join(sorted(str))
        if sorted_str in result:
            result[sorted_str].append(str)
        else:
            result[sorted_str] = [str]

    return list(result.values())  


###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestGroupAnagrams(unittest.TestCase):
    def test_empty_list(self):
        strs = [""]
        self.assertEqual(groupAnagrams(strs), [[""]])
    
    def test_single_string(self):
        strs = ["a"]
        self.assertEqual(groupAnagrams(strs), [["a"]])

    def test_one(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        solution = [["bat"],["nat","tan"],["ate","eat","tea"]]

        sorted_solution = [sorted(inner_list) for inner_list in solution]
        function_return = [sorted(inner_list) for inner_list in groupAnagrams(strs)]
        self.assertCountEqual(function_return, sorted_solution)

if __name__ == "__main__":
    unittest.main() 
