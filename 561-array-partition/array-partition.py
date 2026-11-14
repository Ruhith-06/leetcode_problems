class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        sum = 0
        n = len(nums)
        while(i < n):
            sum += nums[i]
            i += 2
        return sum