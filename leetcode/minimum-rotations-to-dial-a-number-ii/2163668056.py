class Solution:
    def minRotations(self, n: int, s: str) -> int:
        def calc(a, b):
            diff = abs(int(a)-int(b))
            return min(diff, 10-diff)

        prefix = [0]*n 
        prefix[0] = calc('0', s[0])
        for i in range(1, n):
            prefix[i] = prefix[i-1]+calc(s[i-1], s[i])

        ans = prefix[n-1]
        suffix = [0]*n 
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1]+calc(s[i], s[i+1])

        for k in range(n):
            if k==0:
                res = calc('0', s[n-1])+suffix[0]
            else:
                res = prefix[k-1]+calc(s[k-1], s[n-1])+suffix[k]
            ans = min(ans, res)
        return ans