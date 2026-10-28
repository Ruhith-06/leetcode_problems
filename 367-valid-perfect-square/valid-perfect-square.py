class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        i = 0
        j = num
        
        while(i<j):
            mid = (i + j)//2
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num:
                j = mid
            else:
                i = mid+1
        return False