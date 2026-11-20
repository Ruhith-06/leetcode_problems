class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i != '#':
                stack1.append(i)
            else:
                if not stack1:
                    pass
                else:
                    stack1.pop()

        for i in t:
            if i != '#':
                stack2.append(i)
            else:
                if not stack2:
                    pass
                else:
                    stack2.pop()
        
        if stack1 == stack2:
            return True
        return False