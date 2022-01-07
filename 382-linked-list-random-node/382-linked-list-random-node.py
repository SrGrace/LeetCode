# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        # self.range = list()
        # while(head):
        #     self.range.append(head.val)
        #     head = head.next
        
        self.head = head

    def getRandom(self) -> int:
        # idx = int(random.random()*len(self.range))
        # return self.range[idx]
        
        cur = self.head
        res, k = 0, 1  # rand element (choosen val), k element (1 in this case, the scope)
        while(cur):
            if random.random() < 1/k:
                res = cur.val
            k += 1
            cur = cur.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()