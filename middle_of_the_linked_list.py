# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        middle = [head]
        while (middle[-1].next):
            middle.append(middle[-1].next)
        return middle[len(middle)//2]
