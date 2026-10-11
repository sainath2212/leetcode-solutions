class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        d = {}
        def recur(i, canBuy, cap):
            key = (i, canBuy, cap)
            if key in d:return d[key]
            if i>=len(prices) or cap==k:return 0 
            nt = recur(i+1, canBuy, cap)
            if canBuy:
                t = recur(i+1, False, cap)-prices[i]
            else:
                t = recur(i+1, True, cap+1)+prices[i]
            d[key] = max(t, nt)
            return d[key]
        return recur(0, True, 0)