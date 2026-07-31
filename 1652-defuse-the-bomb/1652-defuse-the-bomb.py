from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        if k == 0:
            return [0] * n

        ans = [0] * n

        if k > 0:
            window = sum(code[1:k + 1])
            ans[0] = window

            for i in range(1, n):
                window -= code[i]
                window += code[(i + k) % n]
                ans[i] = window

        else:
            k = -k
            window = sum(code[n - k:])
            ans[0] = window

            for i in range(1, n):
                window -= code[(i - k - 1 + n) % n]
                window += code[i - 1]
                ans[i] = window

        return ans