# You are given two non-empty linked lists
#   representing two non-negative integers.
# The digits are stored in reverse order,
#   and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers
#  do not contain any leading zero,
#  except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        current = self
        while current:
            yield current.val
            current = current.next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        aux_node = ListNode()
        for val1, val2 in zip(l1, l2):
            aux_node.val = val1 + val2
        return aux_node
