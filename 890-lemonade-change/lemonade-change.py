class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        coin5 = 0
        coin10 = 0
        coin20 = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                coin5 += 1
            elif bills[i] == 10 and coin5 >= 1:
                coin10 += 1
                coin5 -= 1
            elif bills[i] == 20 and coin10 >= 1 and coin5 >=1:
                coin10 -= 1
                coin5 -= 1
                coin20 += 1
            elif bills[i] == 20 and coin5 >= 3 :
                coin5 -= 3
                coin20 += 1
            else:
                return False
        return True
            