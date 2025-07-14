# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        no = ''

        while current is not None:
            no += str(current.val)
            current = current.next

        return int(no, 2) # Convets a string to base 2 integer
# 1290. Convert Binary Number in a Linked List to Integer
