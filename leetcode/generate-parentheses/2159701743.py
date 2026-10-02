class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def backtrack(str, o, c):
            if len(str)==2*n:
                res.append(str)
                return 
            if o<n: backtrack(str+"(", o+1, c)
            if c<o:backtrack(str+")", o, c+1)
        backtrack("", 0, 0)
        return res