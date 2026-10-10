class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        d = {}
        def recur(i, j):
            if (i, j) in d:return d[(i, j)]
            if i>=len(text1) or j>=len(text2):return 0 
            if text1[i]==text2[j]:
                d[(i, j)] = 1+recur(i+1, j+1)
            else:
                d[(i, j)] = max(recur(i+1, j), recur(i, j+1))
            return d[(i, j)]
        return recur(0, 0)