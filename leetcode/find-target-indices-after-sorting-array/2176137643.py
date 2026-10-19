class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count = 0 
        dup = 0 
        for i in nums:
            if i<target:
                count+=1
            elif i==target:
                dup+=1 
        ans = []
        for i in range(count, count+dup):
            ans.append(i)
        return ans