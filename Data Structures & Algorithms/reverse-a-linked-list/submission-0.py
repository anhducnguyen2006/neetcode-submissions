# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trail = head
        if trail == None:
            return None
        curr = head.next
        trail.next = None
        while curr != None:
            ahead = curr.next
            curr.next = trail
            trail = curr
            curr = ahead
        return trail
        