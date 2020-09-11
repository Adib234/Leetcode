# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a = []

        while head:
            a.append(head.val)
            head = head.next
        return True if a == a[::-1] else False
