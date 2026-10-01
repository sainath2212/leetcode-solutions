class Solution:
    def rob(self, nums: list[int]) -> int:
        d = {}
        def recur(i, j):
            if i>j:return 0 
            if (i, j) in d:return d[(i, j)]
            d[(i, j)] = max(recur(i+1, j), recur(i+2, j)+nums[i])
            return d[(i, j)]
        if len(nums)==1:
            return nums[0]
        return max(recur(0, len(nums)-2), recur(1, len(nums)-1))