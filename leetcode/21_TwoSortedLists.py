# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return head.next

class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = list1
        n2 = list2
        finalSol = ListNode(0)
        p = finalSol

        while True:
            if n1 is None:
                p.next = n2
                break
            if n2 is None:
                p.next = n1
                break
            if n1.val <= n2.val:
                p.next = n1
                p = p.next
                n1 = n1.next
            else:
                p.next = n2
                p = p.next
                n2 = n2.next

        return finalSol.next



n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n1.next = n3
n3.next = n5
n5.next = n7
n2.next = n4
n4.next = n6
n6.next = n8

result = Solution2().mergeTwoLists(n1, n2)
assert result is n1
assert n1.next is n2
assert n2.next is n3
assert n3.next is n4
assert n4.next is n5
assert n5.next is n6
assert n6.next is n7
assert n7.next is n8
