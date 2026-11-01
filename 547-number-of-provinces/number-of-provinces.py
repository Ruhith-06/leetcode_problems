class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        count=0
        q=[]
        for i in range(n):
            if visited[i]==False:
                count+=1
                visited[i]=True
                q.append(i)
            while len(q)>0:
                a=q.pop()
                for j in range(n):
                    if isConnected[a][j]==1 and visited[j]==False:
                        q.append(j)
                        visited[j]=True
        return count