class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Create frequency dictionary
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Create Max Heap using negative frequency
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))

        # Step 3: Extract top k frequent elements
        ans = []

        for i in range(k):
            count, num = heapq.heappop(heap)
            ans.append(num)

        return ans