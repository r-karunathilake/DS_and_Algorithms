""" Question 141: Linked List Cycle 

Description: Given head, the head of a linked list, determine 
             if the linked list has a cycle in it. There is a cycle 
             in a linked list if there is some node in the list that 
             can be reached again by continuously following the next 
             pointer. Internally, pos is used to denote the index of 
             the node that tail's next pointer is connected to. 
             Note that pos is not passed as a parameter.Return true 
             if there is a cycle in the linked list. 
             Otherwise, return false.

Constraints:
               -10^5 <= Node.value <= 10^5
"""
from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
    # Linked list needs 1+ nodes to create a cycle 
    if not head or not head.next:
        return False

    tortoise = head
    hare = head.next

    while tortoise != hare:
        if not hare or not hare.next:
            return False

        tortoise = tortoise.next
        hare = hare.next.next

    return True

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestLinkedListCycleDetection(unittest.TestCase):
    def test_no_cycle(self):
        # Test case with no cycle
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.assertFalse(hasCycle(head))

    def test_cycle(self):
        # Test case with a cycle
        head = ListNode(1, ListNode(2, ListNode(3)))
        head.next.next.next = head  # Creating a cycle
        self.assertTrue(hasCycle(head))

    def test_single_node_cycle(self):
        # Test case with a cycle in a single-node list
        head = ListNode(1)
        head.next = head  # Creating a cycle
        self.assertTrue(hasCycle(head))

    def test_empty_list(self):
        # Test case with an empty list
        head = None
        self.assertFalse(hasCycle(head))

    def test_two_node_cycle(self):
        # Test case with a cycle in a two-node list
        head = ListNode(1, ListNode(2))
        head.next.next = head  # Creating a cycle
        self.assertTrue(hasCycle(head))

if __name__ == '__main__':
    unittest.main()
