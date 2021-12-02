# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # have fast and slow nodes
        # fast has head start of size 'n'
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
            
        # have to check if n is actually size of LL
        if not fast:
            return head.next    
        
        # if we now go to last node
        # slow pointer will be before nth node from end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # else we can just skip that nth node now
        slow.next = slow.next.next
        return head
        