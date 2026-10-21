class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                a = int(num1[i])
                b = int(num2[j])

                product = a * b + res[i + j + 1]

                res[i + j + 1] = product % 10
                res[i + j] += product // 10

        return ''.join(map(str, res)).lstrip('0') or '0'
