class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr=sum(nums[:k])
        maxs=curr
        for i in range(k,len(nums)):
            curr+=nums[i]-nums[i-k]
            maxs=max(maxs,curr)
        return maxs/k