class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        d = {}
        def recur(s):
            if s in d:return d[s]
            ans = []
            for i, ch in enumerate(s):
                if ch in "-+*":
                    left = recur(s[:i])
                    right = recur(s[i+1:])
                    for a in left:
                        for b in right:
                            if ch=="+":
                                ans.append(a+b)
                            elif ch=="-":
                                ans.append(a-b)
                            elif ch=="*":
                                ans.append(a*b)
            if not ans:
                ans.append(int(s))
            d[s] = ans 
            return ans 
        return recur(expression)

