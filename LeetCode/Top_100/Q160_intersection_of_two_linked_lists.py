""" Question 160: Intersectino of Two Linked Lists

Description: Given the heads of two singly linked-lists headA and headB, return 
             the node at which the two lists intersect. If the two linked lists 
             have no intersection at all, return None. 

             Return the head of the merged linked list. 

Constraints:
               1 <= list.length <= 3 * 10^4
               1 <= node.val    <= 10^5

Note: that the linked lists must retain their original structure after the 
      function returns.
"""
from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: Optional[Node], headB: Optional[Node]) -> Optional[Node]:
    if not headA or not headB:
        return None 

    nodeA, nodeB = headA, headB
    while nodeA != nodeB:
        """ Switch node 'pointers' to account for possible length 
            difference between the linked lists. 
            
            e.g.
                list1 = [4, 1, 8, 4, 5]
                list2 = [5, 6, 1, 8, 4, 5]
                targetNode = 8

                Iteration 1:

                    [4, 1, 8, 4, 5]
                     ^
                     |
                    nodeA
                    
                    [5, 6, 1, 8, 4, 5]
                     ^
                     |
                    nodeB

                ...

                Iteration 6 (Note the pointer A switched lists!):

                    [4, 1, 8, 4, 5]
                    
                    [5, 6, 1, 8, 4, 5]
                     ^              ^
                     |              |
                    nodeA          nodeB
                
                Iteration 7 (Note the pointer B switched lists!):

                    [4, 1, 8, 4, 5]
                     ^
                     |
                    node B
                    
                    [5, 6, 1, 8, 4, 5]
                        ^          
                        |              
                      nodeA        

                ...
                
                Iteration 9 (found the target node!):

                    [4, 1, 8, 4, 5]
                           ^
                           |
                         node B
                    
                    [5, 6, 1, 8, 4, 5]
                              ^          
                              |              
                            nodeA  
        """
        nodeA = headB if nodeA is None else nodeA.next
        nodeB = headA if nodeB is None else nodeB.next

    return nodeA

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestListMerge(unittest.TestCase):
    def create_linked_list(self, values: list) -> Optional[Node]:
        nodes = [Node(value) for value in values]
        for idx, node in enumerate(nodes):
            try:
                node.next = nodes[idx + 1]
            except IndexError:
                node.next = None
        
        return nodes[0]
    
    def test_empty_lists(self):
        self.assertEqual(getIntersectionNode([], []), None)

    def test_non_intersecting_lists(self):
        list1 = self.create_linked_list([1, 2, 3])
        list2 = self.create_linked_list([4, 5, 6])

        self.assertEqual(getIntersectionNode(list1, list2), None)

    def test_intersecting_same_length_lists(self):
        intersectionNode = Node(5)
        list1 = Node(4, Node(1, intersectionNode))
        list2 = Node(5, Node(0, intersectionNode))

        self.assertEqual(getIntersectionNode(list1, list2), intersectionNode)

    def test_intersecting_diff_length_lists(self):
        intersectionNode = Node(9)
        list1 = Node(4, Node(1, intersectionNode))
        list2 = Node(5, Node(0, Node(5, intersectionNode)))

        self.assertEqual(getIntersectionNode(list1, list2), intersectionNode)

if __name__ == "__main__":
    unittest.main() 
