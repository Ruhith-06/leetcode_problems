class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        l = []
        for i in stones:
            l.append(-i)
        heapq.heapify(l)

        while(len(l)>1):
            fst = -heapq.heappop(l)
            scnd = -heapq.heappop(l)

            if fst != scnd:
                heapq.heappush(l, -(fst-scnd))
        if len(l) == 0:
            return 0
        else:
            return -l[-1]