""" Question 211: Design Add and Search Words Data Structure

Description: Design a data structure that supports adding new words and finding 
if a string matches any previously added string.

Implement the WordDictionary class:

    - WordDictionary() Initializes the object.
    - void addWord(word) Adds word to the data structure, it can be matched later.
    - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Constraints:

                        1 <= word.length <= 25
    - word in addWord consists of lowercase English letters.
    - word in search consist of '.' or lowercase English letters.
    - There will be at most 2 dots in word for search queries.
    - At most 104 calls will be made to addWord and search.

"""
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False 

class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if not currentNode.children.get(char):
                currentNode.children[char] = TrieNode()
            
            currentNode = currentNode.children[char]
        
        # Mark the ending of the word 
        currentNode.end = True

    def search(self, word:str) -> bool:
        def dfs(idx: int, node: TrieNode) -> bool:
            currentNode = node
            for i in range(idx, len(word)):
                char = word[i]
                if char == '.':
                    for node in currentNode.children.values():
                        # If found atleast one word that matches the word, 
                        # return True.
                        if dfs(i + 1, node):
                            return True 
                    return False 
                else:
                    if not currentNode.children.get(char):
                        return False
                    currentNode = currentNode.children[char]

            return currentNode.end

        return dfs(0, self.root)    
###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestDictionary(unittest.TestCase):

    def test_insert_and_search(self):
        trie = WordDictionary()
        insert = ["bad", "dad", "mad", "pad", "pad"]
        for val in insert:
            trie.addWord(val)

        self.assertTrue(trie.search("bad"))
        self.assertTrue(trie.search("dad"))
        self.assertTrue(trie.search("b.."))
        self.assertFalse(trie.search("p.r"))

if __name__ == "__main__":
    unittest.main() 
