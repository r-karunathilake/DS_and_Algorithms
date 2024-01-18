""" Question 234: Palindrome Linked List 

Description: Given the head of a singly linked list, return True 
             if it is a palindrome or False otherwise. 

Constraints:
                 1 <= number of nodes <= 10^5
                 0 <= node.val        <= 9 
"""

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(startNode: ListNode) -> ListNode:
    prevNode = None
    currentNode = startNode

    while currentNode:
        nextNode = currentNode.next 
        currentNode.next = prevNode
        prevNode = currentNode 
        currentNode = nextNode
    
    return prevNode


def isPalindrome(head: Optional[ListNode]) -> bool:
    # Start at the same point 
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next      # Steps: 1 
        fast = fast.next.next # Steps: 2
    
    # The 'slow' pointer is  now in the middle of the linked list
    reversedList = reverseLinkedList(slow)

    # Compare the first and reversed second half of the linked list
    while reversedList:
        if head.val != reversedList.val:
            return False
        
        head = head.next
        reversedList = reversedList.next

    return True 

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest

class TestTreeTraversal(unittest.TestCase):
    def test_single_val(self):
        head = ListNode(1)
        self.assertTrue(isPalindrome(head))

    def test_long_list(self):
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        self.assertTrue(isPalindrome(head))

    def test_short_list(self):
        head = ListNode(1, ListNode(2))
        self.assertFalse(isPalindrome(head))
    
    def test_longer_list(self):
        head = ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode(3, ListNode(1))))))
        self.assertTrue(isPalindrome(head))

if __name__ == '__main__':
    unittest.main()
