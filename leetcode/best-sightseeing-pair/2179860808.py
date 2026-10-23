class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        besty = values[0]
        maxi = 0 
        for j in range(1, len(values)):
            maxi = max(maxi, besty+values[j]-j)
            besty = max(besty, values[j]+j)
        return maxi 