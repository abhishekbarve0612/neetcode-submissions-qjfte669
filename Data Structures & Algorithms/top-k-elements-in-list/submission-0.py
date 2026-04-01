class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            hash[num] = 1 + hash.get(num, 0)

        arr = []

        for num, count in hash.items():
            arr.append([count, num])

        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res