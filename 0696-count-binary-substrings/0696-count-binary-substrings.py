class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevgs=0
        currgrps=1
        count=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                currgrps+=1
            else:
                prevgs=currgrps
                currgrps=1
            if prevgs>=currgrps:
                count+=1
        return count