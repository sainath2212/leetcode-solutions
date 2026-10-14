class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        ns = sum // 9
        remain = sum % 9
        res = "9" * ns
        if remain > 0:res += str(remain)
        res += "0" * (num - len(res))
        return res