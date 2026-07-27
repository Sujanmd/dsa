class Solution:
    def isHappy(self, n: int) -> bool:
        
        def squaresum(n):
            sum1=0
            while n>0 :
                dig=n%10
                sum1+=dig*dig
                n=n//10
            return sum1
        ans=squaresum(n)
        while True:
            ans=squaresum(ans)
            if abs(ans)<10:
                break
        return True if ans==1 else False
        
