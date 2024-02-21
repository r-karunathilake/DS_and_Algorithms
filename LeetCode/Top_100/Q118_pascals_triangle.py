""" Question 118: Pascal's Triangle

Description: Given an integer numRows, return the first numRows of Pascal's 
             triangle. In Pascal's triangle, each number is the sum of the two 
             numbers directly above it as shown.

Constraints:
                 1 <= numRows <= 30
"""

from typing import List

# Time complexity:  O(numRows^2)
# Space complexity: O(numRows^2)
def generate(numRows: int) -> List[List[int]]:
    # First row 
    triangle = [[1]]
    for i in range(1, numRows):
        row = [1] +  [triangle[i-1][j-1]  + triangle[i-1][j] for j in range(1, i)]  + [1]
        #                            ^                    ^  
        #                            |                    |
        #                    previous top-left     previous top-right
        triangle.append(row)

    return triangle

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestMajorityElement(unittest.TestCase):
    def test_majority_one_row(self):
        expected = [[1]]
        self.assertEqual(generate(1), expected)

    def test_majority_two_row(self):
        expected = [[1], [1, 1]]
        self.assertEqual(generate(2), expected)

    def test_majority_three_row(self):
        expected = [[1], [1, 1], [1, 2, 1]]
        self.assertEqual(generate(3), expected)

    def test_majority_four_row(self):
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        self.assertEqual(generate(4), expected)

    def test_majority_five_row(self):
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertEqual(generate(5), expected)

if __name__ == "__main__":
    unittest.main() 
