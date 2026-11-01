class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = [False] * (len(rooms))
        q = []
        q.append(0)
        visited[0] = True
        while(len(q) > 0):
            a=q.pop(0)
            for keys in rooms[a]:
                if visited[keys] == False:
                    q.append(keys)
                    visited[keys] = True
        if False in visited:
            return False
        return True