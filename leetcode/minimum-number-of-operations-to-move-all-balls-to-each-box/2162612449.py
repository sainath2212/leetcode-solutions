class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        ans = [0]*n 
        balls = 0 
        moves = 0 
        for i in range(n):
            ans[i]+=moves 
            balls+=int(boxes[i])
            moves+=balls 
        balls = 0 
        moves = 0 
        for i in range(n-1, -1, -1):
            ans[i]+=moves 
            balls+=int(boxes[i])
            moves+=balls 
        return ans