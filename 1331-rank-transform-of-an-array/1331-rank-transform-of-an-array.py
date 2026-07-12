class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        temp = sorted(arr)

        rank = 1
        for num in temp:
            if num not in d:
                d[num] = rank
                rank += 1

        ans = []
        for num in arr:
            ans.append(d[num])

        return ans
        