class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        first = second = 0
        hash, maxF = {}, 0
        maxRes = 0

        while second < len(s):
            hash[s[second]] = 1 + hash.get(s[second], 0)

            maxF = max(maxF, hash[s[second]])

            while ((second - first + 1) - maxF) > k:
                hash[s[first]] -= 1
                first += 1

            maxRes = max(maxRes, second - first + 1)

            second += 1
        return maxRes

            