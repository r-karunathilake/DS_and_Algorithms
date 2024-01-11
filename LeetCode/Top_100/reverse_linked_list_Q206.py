""" Question 206: Reverse Linked List

Description: Given the head of a singly linked list, reverse the list, 
             and return the reversed list. 

Constraints:
                 0 <= number of nodes <= 5000
             -5000 <= node.val        <= 5000
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next 

from typing import Optional

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    prev = None
    current = head 

    while(current):
        next = current.next 
        current.next = prev 
        prev = current
        current = next 

    return prev # The new head 

def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:

    if((head is None) or (head.next is None)):
        return head 

    rem = reverseListRecursive(head.next)
   
    head.next.next = head
    head.next = None

    return rem


###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestReverseLinkedList(unittest.TestCase):
    def create_linked_list(self, values):
        if not values:
            return None

        nodes = [ListNode(value) for value in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        return nodes[0]

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def test_reverse_linked_list(self):
        # Test case 1
        input_list = self.create_linked_list([1, 2, 3, 4, 5])
        expected_output = [5, 4, 3, 2, 1]
        reversed_list = reverseList(input_list)
        self.assertEqual(self.linked_list_to_list(reversed_list), expected_output)

        # Test case 2
        input_list = self.create_linked_list([1, 2])
        expected_output = [2, 1]
        reversed_list = reverseList(input_list)
        self.assertEqual(self.linked_list_to_list(reversed_list), expected_output)

    def test_reverse_linked_list_recursive(self):
        # Test case 1
        input_list = self.create_linked_list([1, 2, 3, 4, 5])
        expected_output = [5, 4, 3, 2, 1]
        reversed_list = reverseListRecursive(input_list)
        self.assertEqual(self.linked_list_to_list(reversed_list), expected_output)

        # Test case 2
        input_list = self.create_linked_list([1, 2])
        expected_output = [2, 1]
        reversed_list = reverseListRecursive(input_list)
        self.assertEqual(self.linked_list_to_list(reversed_list), expected_output)

if __name__ == '__main__':
    unittest.main()




