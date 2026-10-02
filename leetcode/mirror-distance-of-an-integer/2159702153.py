class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        x = n 
        while x:
            rev = rev*10+x%10 
            x//=10 
        return abs(n-rev)