""" Question 208: Implement Trie (Prefix Tree)

Description: A trie (pronounced as "try") or prefix tree is a tree data structure 
used to efficiently store and retrieve keys in a dataset of strings. There are 
various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Constraints:

              1 <= word.length, prefix.length <= 2000
    
    - Word and prefix consist only of lowercase English letters.
    - At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False 

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if not currentNode.children.get(char):
                currentNode.children[char] = TrieNode()
            
            currentNode = currentNode.children[char]
        
        # Mark the ending of the word 
        currentNode.end = True

    def search(self, word:str) -> bool:
        currentNode = self.root
        for char in word:
            if not currentNode.children.get(char):
                return False 
            
            currentNode = currentNode.children[char]
        
        # We have gone through all the characters of the 
        # given word. Return if the current node is marked as 
        # the end of a word.
        return currentNode.end 
    
    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for char in prefix:
            if not currentNode.children.get(char):
                return False

            currentNode = currentNode.children[char]

        # We've gone through all the characters in 'prefix' and
        # they are in the Trie
        return True 
    
###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestTrie(unittest.TestCase):

    def test_insert_and_search(self):
        trie = Trie()
        insert = ["apple", "app"]
        for val in insert:
            trie.insert(val)

        self.assertTrue(trie.search("apple"))
        self.assertTrue(trie.search("app"))
        self.assertFalse(trie.search("orange"))
    
    def test_prefix(self):
        trie = Trie()
        insert = ["dog", "cat", "bird", "turtle", "rabbit"]
        for val in insert:
            trie.insert(val)

        self.assertTrue(trie.startsWith("turt"))
        self.assertFalse(trie.startsWith("god"))


if __name__ == "__main__":
    unittest.main() 
