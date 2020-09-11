# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack = []
        sum = 0
        while (head):
            stack.append(head.val)
            head = head.next
        i = 0
        while (len(stack) != 0):
            sum += stack.pop()*(2**i)
            i += 1
        return sum
