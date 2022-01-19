# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slw, fst = head, head
        while(slw and fst and fst.next):
            slw = slw.next
            fst = fst.next.next
            if slw == fst:
                slw1 = head
                while(slw != slw1):
                    slw = slw.next
                    slw1 = slw1.next
                return slw
        return None
    
    