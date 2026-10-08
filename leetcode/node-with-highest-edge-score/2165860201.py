class Solution:
    def edgeScore(self, edges: list[int]) -> int:
        n = len(edges)
        score = [0]*n 
        for i in range(n):
            score[edges[i]]+=i 
        maxi = 0 
        ans = -1 
        for i in range(n):
            if score[i]>maxi:
                maxi = score[i]
                ans = i 
        return ans