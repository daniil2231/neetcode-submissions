class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = float("inf")

        for p in prices:
            if p < buy:
                buy = p
            elif p > buy:
                res += p - buy
                buy = p

        return res