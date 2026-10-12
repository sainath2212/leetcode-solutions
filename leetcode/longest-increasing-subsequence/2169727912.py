class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        d = [[-1]*(n+1) for i in range(n+1)]
        def recur(i, pre):
            if i==len(nums):return 0 
            if d[i][pre]!=-1: return d[i][pre]
            t = 0 
            if pre==-1 or nums[i]>nums[pre]:
                t = 1+recur(i+1, i)
            nt = recur(i+1, pre)
            d[i][pre] = max(t, nt)
            return d[i][pre]
        return recur(0, -1)