# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-101)
        dummy_head.next = head
        
        cur = dummy_head
        while(cur.next):
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next