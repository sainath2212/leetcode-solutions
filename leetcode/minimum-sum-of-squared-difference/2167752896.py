class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = sorted([abs(a - b) for a, b in zip(nums1, nums2)], reverse=True)
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.append(0)

        for i in range(len(diff) - 1):
            count = i + 1
            gap = diff[i] - diff[i + 1]
            cost = gap * count

            if k >= cost:
                k -= cost
                diff[i] = diff[i + 1]
            else:
                level = diff[i] - k // count
                remainder = k % count

                ans = sum(d * d for d in diff[i + 1:])
                ans += remainder * (level - 1) ** 2
                ans += (count - remainder) * level ** 2
                return ans

        return 0