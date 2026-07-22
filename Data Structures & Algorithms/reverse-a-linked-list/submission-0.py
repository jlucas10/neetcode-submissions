# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        # while curr is not null loop, end when null (no more nodes)
        # T O(n)
        while curr: 
            #temp 
            nxt = curr.next 
            curr.next = prev
            prev = curr
            #temp variable nxt
            curr = nxt
        return prev 