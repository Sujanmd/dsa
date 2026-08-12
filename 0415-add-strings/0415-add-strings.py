class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n=len(num1)-1
        m=len(num2)-1
        res=[]
        remainder=0
        while n>=0 or m>=0 or remainder:
            total=(
                (int(num1[n]) if n>=0 else 0)+
            (int(num2[m]) if m>=0 else 0)+ remainder)
            res.append(str(total%10))
            remainder=total//10
            n-=1
            m-=1
        return "".join(reversed(res))