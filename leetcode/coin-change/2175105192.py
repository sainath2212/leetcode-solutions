class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        d = {}
        def recur(rem):
            if rem==0:return 0 
            if rem<0:return float('inf')
            if rem in d:return d[rem]
            ans = float('inf')
            for coin in coins:
                ans = min(ans, 1+recur(rem-coin))
            d[rem] = ans 
            return ans 
        res = recur(amount)
        return res if res!=float('inf') else -1