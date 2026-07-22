class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[0] * (i+1) for i in range(n)]
        for i in range(n):
            dp[n-1][i]=triangle[n-1][i]
        for rows in range(n-2,-1,-1):
            for cols in range(rows+1):
                dp[rows][cols]=triangle[rows][cols]+min(dp[rows+1][cols],dp[rows+1][cols+1])
        return dp[0][0]
        