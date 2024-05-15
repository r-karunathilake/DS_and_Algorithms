""" Question 143: Reorder List

Description: You are given the head of a singly linked-list. The list 
             can be represented as:

                L0 → L1 → … → Ln - 1 → Ln

                Reorder the list to be on the following form:

                L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

Constraints:
    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000
"""
class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val 
        self.next = next 

from typing import Optional
def reorderList(head: Optional[ListNode]) -> None:
    slow = fast = head
    # Find the middle of the linked list
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next 

    # In place reversal of the right half of the list 
    prev, current  = None, slow.next 
    
    # Make sure the left part of the linked list ends on None
    slow.next = None
    while current:
        next = current.next
        current.next = prev 
        prev = current 
        current = next 

    # New head of the two seperate linked lists 
    first = head 
    second = prev 

    # Merge the two linked lists now 
    while second: 
        first.next, first = second, first.next 
        second.next, second = first, second.next

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestRotatedMin(unittest.TestCase):
    def navigateList(head: ListNode) -> list[int]:
        result = []
        while head:
            result.append(head.val)
            head = head.next 

        return result 

    def test_one(self):
        list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        solution = [1, 4, 2, 3]
        reorderList(list)
        self.assertEqual(TestRotatedMin.navigateList(list), solution)
    
    def test_two(self):
        list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        solution = [1,5,2,4,3]
        reorderList(list)
        self.assertEqual(TestRotatedMin.navigateList(list), solution)
    
if __name__ == "__main__":
    unittest.main() 
