class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def calc(m):
            c = 1
            s = 0 
            for i in nums:
                if s+i<=m:
                    s+=i 
                else:
                    c+=1 
                    s = i 
            return c<=k
        l = max(nums)
        h = sum(nums)
        while l<h:
            m = (l+h)//2 
            if calc(m):
                h = m 
            else:
                l = m+1 
        return l 