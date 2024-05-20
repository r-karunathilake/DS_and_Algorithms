""" Question 212: Word Search II

Description: Given an m x n board of characters and a list of strings words, 
             return all words on the board.

             Each word must be constructed from letters of sequentially adjacent 
             cells, where adjacent cells are horizontally or vertically 
             neighboring. The same letter cell may not be used more than once 
             in a word.
Constraints:

                       m == board.length
                       n == board[i].length
                       
                       1 <= m, n            <= 12
                       1 <= words.length    <= 3 * 104
                       1 <= words[i].length <= 10

     - board[i][j] is a lowercase English letter.
     - words[i] consists of lowercase English letters.
     - All the strings of words are unique.
"""
class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.end = False 

class Trie():
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if not currentNode.children.get(char):
                currentNode.children[char] = TrieNode()

            currentNode = currentNode.children[char]
        
        # Mark the end of the word in the trie data structure 
        currentNode.end = True 
    
    def search(self, word: str) -> True:
        currentNode = self.root
        for char in word:
            if not currentNode.children.get(char):
                return False 
            
            currentNode = currentNode.children[char]
        return True 

class Solution:
    def findWords(self, board: list[list[int]], words: list[str]) -> list[str]:
        word_trie = Trie()
        for word in words:
            word_trie.addWord(word)
        
        visited = set()
        def dfs(r: int, c: int, node: TrieNode, word: str) -> None:
            # Check the row bounds 
            if r < 0 or r >= len(board):
                return 
            
            # Check the column bounds 
            if c < 0 or c >= len(board[0]):
                return 
            
            # Check if the current position has already been visisted
            if (r, c) in visited:
                return 
            
            # Check if the character at position 'row' & 'column' exist in the trie
            if board[r][c] not in node.children:
                return 
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c] # Add the character to the word 

            # If we reach the end of a word
            if node.end:
                result.add(word)
                node.end = False # Avoid duplicate entries 

            dfs(r - 1, c, node, word) 
            dfs(r + 1, c, node, word)  
            dfs(r, c - 1, node, word) 
            dfs(r, c + 1, node, word) 

            visited.remove((r, c)) # Finished checking word from this position 

        result = set()
        for row in range(len(board)):
            for column in range(len(board[0])):
                dfs(row, column, word_trie.root, "")

        return list(result)


###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestWordSearch(unittest.TestCase):

    def test_one(self):
        obj = Solution()
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        solution = ["eat","oath"]

        self.assertCountEqual(obj.findWords(board, words), solution)

    def test_two(self):
        obj = Solution()
        board = [["a","b"],["c","d"]]
        words = ["abcb"]
        solution = []

        self.assertCountEqual(obj.findWords(board, words), solution)

if __name__ == "__main__":
    unittest.main() 
