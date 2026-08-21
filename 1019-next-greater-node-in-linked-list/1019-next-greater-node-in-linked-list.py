class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        lst = []
        curr = head

        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        result = [0] * len(lst)
        st = []
        for i, val in enumerate(lst):
            while st and lst[st[-1]] < val:
                ind = st.pop()
                result[ind] = val
            st.append(i)
        return result