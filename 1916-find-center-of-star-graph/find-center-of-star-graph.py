class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        x = edges[0]
        for i in x:
            if i in edges[1]:
                return i

        