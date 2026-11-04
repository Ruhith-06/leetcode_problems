class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = nums1+nums2
        arr.sort()
        l = len(arr)
        if l % 2 == 0:
            mid = l//2
            return (arr[(mid-1)] + arr[mid])/2.0
        else:
            return arr[l//2]
        