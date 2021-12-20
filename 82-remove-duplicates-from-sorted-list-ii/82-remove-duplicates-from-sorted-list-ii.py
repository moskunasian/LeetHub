# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # sentinal node set to before head
        # pred will be up until the repeating portion of LL
        
        sentinal = ListNode(0, head)
        pred = sentinal
        
        while head:
            # if we are at beginning of dupes, begin skipping
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
                
            head = head.next
            
        return sentinal.next
            