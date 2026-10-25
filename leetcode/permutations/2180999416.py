class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def recur(path, used):
            if len(path)==len(nums):
                res.append(path[:])
                return 
            for i in range(len(nums)):
                if used[i]:continue 
                used[i] = True 
                path.append(nums[i])
                recur(path, used)
                path.pop()
                used[i] = False 
        used = [False]*len(nums)
        recur([], used)
        return res