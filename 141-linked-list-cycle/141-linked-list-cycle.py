# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slw, fst = head, head
        while(slw and fst and fst.next):
            slw = slw.next
            fst = fst.next.next
            if slw == fst:
                return 1
        return 0
    