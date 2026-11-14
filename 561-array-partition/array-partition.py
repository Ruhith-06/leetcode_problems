class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        sum = 0
        n = len(nums)
        for i in range(0,len(nums),2):
            sum += nums[i]
        return sum