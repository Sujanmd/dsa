class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl=0
        left=0
        charset=set()
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[i])
            maxl=max(maxl,i-left+1)
        return maxl