class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        j = 1
        while(j < len(nums)):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1
                
        return len(nums)