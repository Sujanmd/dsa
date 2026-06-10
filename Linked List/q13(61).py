# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        if not head or not head.next or k == 0:
            return head
        
        curr=head
        while curr:
            count+=1
            curr=curr.next
        
        k=k%count
        
        node=count-k
        if node==count or node==0:
            return head
        curr=head

        for _ in range(node-1):
            curr=curr.next
        breakp=curr
        

        new=curr.next
        breakp.next=None
        temp=new
        while new.next:
            new=new.next
        new.next=head
        return temp
        