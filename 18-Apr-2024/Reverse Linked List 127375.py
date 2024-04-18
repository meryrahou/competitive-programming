# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        # change next of head to null
        nexts = None
        while ptr:
            store = ptr.next
            ptr.next = nexts
            nexts = ptr
            ptr = store
        
        return nexts