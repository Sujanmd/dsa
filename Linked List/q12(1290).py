# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        val=0
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        curr=head
        count-=1
        while curr:
            val=val+2**count*curr.val
            count-=1
            curr=curr.next
        return val