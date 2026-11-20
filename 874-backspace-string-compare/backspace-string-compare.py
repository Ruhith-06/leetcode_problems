class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def solve(string):
            stack = []

            for i in string:
                if i != '#':
                    stack.append(i)
                else:
                    if not stack:
                        pass
                    else:
                        stack.pop()
            return ''.join(stack)
        return solve(s) == solve(t)