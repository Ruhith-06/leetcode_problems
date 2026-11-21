class Solution(object):
    def maxArea(self, height):
        maxi = 0
        l = len(height)
        i = 0
        j = l-1

        while i < j:
            w = (j-i)
            h = min(height[i],height[j])

            a = w * h
            maxi = max(maxi,a)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxi



        
                