class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        first=strs[0]
        second=strs[-1]
        i=0
        j=0
        while i<len(first) and j<len(second) and first[i]==second[j]:
            i+=1
            j+=1
        return first[:i]

