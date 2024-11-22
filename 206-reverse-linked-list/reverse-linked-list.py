# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            tempnext = cur.next #4
            cur.next = prev #2
            prev = cur # 3
            cur = tempnext #4
        return prev   

        
        