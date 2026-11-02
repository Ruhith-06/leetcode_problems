class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        l = []
        for i in range(l1):
            flag = True
            for j in range(l2):
                if nums1[i] == nums2[j]:
                    for k in range(j+1,l2):
                        if nums2[k] > nums1[i]:
                            l.append(nums2[k])
                            flag = False
                            break
                    
            if flag:
                l.append(-1)
                    
                        
        return l