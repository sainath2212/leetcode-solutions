class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        sett = sorted(set(nums))
        
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        ans = []

        while d:
            for i in sett:
                if i in d:
                    ans.append(i)
                    d[i] -= 1
                    
                    if d[i] == 0:
                        del d[i]

        return ans