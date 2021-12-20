# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        while head:
            # ex:
            
            # saving new head as 2 instead of 1
            nextHead = head.next
            
            # old next is None, prev is 1
            head.next, prev = prev, head
            
            # head is 2
            head = nextHead
        return prev