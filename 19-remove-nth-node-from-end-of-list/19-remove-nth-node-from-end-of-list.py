# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slw = fst = head
        for _ in range(n):
            fst = fst.next

        if not fst:
            return head.next
        
        while(fst.next):
            fst = fst.next
            slw = slw.next
            
        slw.next = slw.next.next
        
        return head
    
    