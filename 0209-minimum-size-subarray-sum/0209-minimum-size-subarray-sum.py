class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        sums = 0
        ans = float('inf')

        for r in range(n):
            sums += nums[r]

            while sums >= target:
                ans = min(ans, r - l + 1)
                sums -= nums[l]
                l += 1

        return 0 if ans == float('inf') else ans