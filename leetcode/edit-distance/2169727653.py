class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        d = {}
        def recur(i, j):
            if (i, j) in d:return d[(i, j)]
            if i<0:return j+1
            if j<0:return i+1 
            if word1[i]==word2[j]:
                d[(i, j)] = recur(i-1, j-1)
            else:
                one = recur(i-1, j-1)
                two = recur(i-1, j)
                three =recur(i, j-1)
                d[(i, j)] = 1+min(one, two, three)
            return d[(i, j)]
        return recur(len(word1)-1, len(word2)-1)