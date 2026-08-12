class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxl=0
        freq={}
        l=0
        for r in range(len(nums)):
            freq[nums[r]]=freq.get(nums[r],0)+1
            while freq[nums[r]]>k:
                freq[nums[l]]-=1
                l+=1
            maxl=max(maxl,r-l+1)
           
        return maxl