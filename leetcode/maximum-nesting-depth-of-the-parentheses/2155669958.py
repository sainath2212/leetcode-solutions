class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0 
        d = 0 
        for i in s:
            if i=="(":
                d+=1 
                maxi = max(maxi, d)
            elif i==")":
                d-=1 
        return maxi