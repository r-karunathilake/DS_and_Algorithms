""" Question 21: Merge Two Sorted Lists

Description: You are given the heads of two sorted linked lists 'list1' and 'list2'.
             Merge the two lists into one sorted list. The list should be made by
             splicing together the nodes of the first two lists. 

             Return the head of the merged linked list. 

Constraints:
               0 <= list.length <= 50
            -100 <= node.val    <= 100

Note: both 'list1' and 'list2' are sorted in ascending order. 
"""
from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""The solutions big O is as follows:
   Time Complexity:  O(N)
   Space Complexity: O(1)

   Where N is the TOTAL number of integers in both lists 
"""
def mergeLists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    false_head = Node()
    current_node = false_head

    # If both of the linked lists are of equal length 
    while list1 and list2:   
        if list1.val <= list2.val:
            current_node.next = list1 
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next 

        current_node = current_node.next
        
    # Check if both linked lists are fully processed
    if list1:
        current_node.next = list1
    elif list2:
        current_node.next = list2

    return false_head.next

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestListMerge(unittest.TestCase):
    def create_linked_list(self, values: list=[]) -> Optional[Node]:
        if not values:
            return None

        nodes = [Node(value) for value in values]
        for idx, node in enumerate(nodes):
            try:
                node.next = nodes[idx + 1]
            except IndexError:
                node.next = None
        
        return nodes[0]

    def linked_list_to_list(self, head: Node) -> list:
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next

        return result

    def test_empty_lists_merge(self):
        list1 = self.create_linked_list()
        list2 = self.create_linked_list()

        self.assertEqual(self.linked_list_to_list(mergeLists(list1, list2)), [])
        
    def test_same_size_lists(self):
        list1 = self.create_linked_list([1, 2, 5])
        list2 = self.create_linked_list([0, 3, 6])

        self.assertEqual(self.linked_list_to_list(mergeLists(list1, list2)), 
                         [0, 1, 2, 3, 5, 6])
    
    def test_different_size_lists(self):
        list1 = self.create_linked_list([1, 2, 3])
        list2 = self.create_linked_list([0, 6, 8, 9])

        self.assertEqual(self.linked_list_to_list(mergeLists(list1, list2)),
                         [0, 1, 2, 3, 6, 8, 9])

    def test_duplicate_values_lists(self):
        list1 = self.create_linked_list([1, 2, 3])
        list2 = self.create_linked_list([0, 3, 6, 6, 7, 8, 9])
    
        self.assertEqual(self.linked_list_to_list(mergeLists(list1, list2)),
                         [0, 1, 2, 3, 3, 6, 6, 7, 8, 9])

if __name__ == "__main__":
    unittest.main() 
