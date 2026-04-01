class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = csum = 0
        hash = {}
        
        for num in nums:
            csum += num
            diff = csum - k

            if csum == k:
                count += 1

            count += hash.get(diff, 0)

            hash[csum] = 1 + hash.get(csum, 0)

        return count