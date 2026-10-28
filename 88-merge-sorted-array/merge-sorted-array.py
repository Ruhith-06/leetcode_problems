class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if m < 1 or n < 1:
            if m < 1:
                nums1[:] = nums2
                return nums1
            elif n < 1:
                return nums1
        nums1[m:] = nums2

        nums1.sort()
        
        

        