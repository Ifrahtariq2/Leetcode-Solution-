# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        array = []
        cur = head
        while cur:
            array.append(cur.val)
            cur = cur.next
        if k != 0 and len(array) != 0:
            k = k % len(array)
        else:
            return head
        array = array[-k:] + array[:-k]
        dumy = ListNode()
        temp = dumy
        for val in array:
            temp.next = ListNode(val) 
            temp = temp.next
        return dumy.next      


