class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        h = len(height)-1
        maxi = 0
        while l<h:
            w = min(height[l], height[h])*(h-l)
            maxi = max(maxi, w)
            if height[l]<height[h]:
                l+=1
            else:
                h -=1
        return maxi