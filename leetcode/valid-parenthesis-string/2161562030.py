class Solution:
    def checkValidString(self, s: str) -> bool:
        op = 0
        cl = 0

        for i in s:
            if i == "(":
                op += 1
                cl += 1
            elif i == ")":
                op -= 1
                cl -= 1
            elif i == "*":
                op -= 1
                cl += 1

            if cl < 0:
                return False

            op = max(0, op)

        return op == 0