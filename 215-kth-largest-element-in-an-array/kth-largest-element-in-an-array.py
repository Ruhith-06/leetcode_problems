class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        l = len(nums)
        for i in range(l-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
            