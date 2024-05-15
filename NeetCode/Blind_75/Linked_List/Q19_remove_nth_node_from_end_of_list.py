""" Question 19: Remove Nth Node From End of List

Description: Given the head of a linked list, remove the nth node from the end 
             of the list and return its head.


Constraints:

    The number of nodes in the list is sz.
                    1 <= sz       <= 30
                    0 <= Node.val <= 100
                    1 <= n        <= sz


    Time Complexity:  O(N)
    Space Complexity: O(1)

Where N is the number of nodes in the linked list. 
"""
class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val 
        self.next = next 

from typing import Optional
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    false_head = ListNode()
    false_head.next = head 

    prev, fast = false_head, false_head

    for _ in range(n + 1):
        fast = fast.next 

    while fast:
        prev = prev.next
        fast = fast.next 
    
    # Remove the node 
    prev.next = prev.next.next 

    return false_head.next


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
        solution = [1, 2, 3]
        removeNthFromEnd(list, 1)
        self.assertEqual(TestRotatedMin.navigateList(list), solution)
    
    def test_two(self):
        list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        solution = [1,3,4,5]
        removeNthFromEnd(list, 4)
        self.assertEqual(TestRotatedMin.navigateList(list), solution)
    
if __name__ == "__main__":
    unittest.main() 
