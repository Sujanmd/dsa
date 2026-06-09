class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = 0
        
        for i in range(n):
            current_count = 0
            for j in range(i, n):
                if nums[j] == 1:
                    current_count += 1
                    max_count = max(max_count, current_count)
                else:
                    break
        
        return max_count