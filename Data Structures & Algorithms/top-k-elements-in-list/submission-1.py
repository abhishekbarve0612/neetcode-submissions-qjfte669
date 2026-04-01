class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1

        heap = []

        for num in hash.keys():
            heapq.heappush(heap, (hash[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result;