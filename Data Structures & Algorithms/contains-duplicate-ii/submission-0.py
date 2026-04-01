class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = set[int]()
        left = 0
        for right in range(len(nums)):
            if right - left > k:
                hash.remove(nums[left])
                left += 1
            if nums[right] in hash:
                return True
            hash.add(nums[right])
        return False