# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative
        # prev = None
        # while(head):
        #     cur = head
        #     head = head.next
        #     cur.next = prev
        #     prev = cur
        #     # print(head, cur, prev)
        #     # print("***")
              
        # return prev
        
        # recursive
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)
        
        
             