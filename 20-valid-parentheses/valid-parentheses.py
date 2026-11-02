class Solution(object):
    def isValid(self, s):
        r=[]
        dist = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for i in s:
            if i in '([{':
                r.append(i)
            else:
                if not r or r[-1] != dist[i]:
                    return False 
                r.pop()
        return len(r) == 0

        