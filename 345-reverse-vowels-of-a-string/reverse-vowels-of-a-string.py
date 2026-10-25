class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        sl = list(s)
        while(i<j):
            if sl[i] in 'aeiouAEIOU' and sl[j] in 'aeiouAEIOU':
                sl[i] , sl[j] = sl[j] , sl[i]
                i += 1
                j -= 1
            elif sl[i] not in 'aeiouAEIOU':
                i += 1
            elif sl[j] not in 'aeiouAEIOU':
                j -= 1
        return ''.join(sl)