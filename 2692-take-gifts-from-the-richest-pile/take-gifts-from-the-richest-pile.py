class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)
        l = []
        
        for i in gifts:
            l.append(-i)
        heapq.heapify(l)

        for i in range(k):
            ele = -heapq.heappop(l)
            ele = int(ele ** 0.5)
            heapq.heappush(l,-ele)
        return -sum(l)
            