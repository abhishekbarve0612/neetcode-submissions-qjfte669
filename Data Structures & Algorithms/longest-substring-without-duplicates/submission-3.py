class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first, second = 0, 1
        maxLen = min(1, len(s))
        counter = maxLen

        while second < len(s):
            if s[second] in s[first:second]:
                maxLen = max(maxLen, counter)
                while first <= second and s[second] in s[first:second]:
                    first += 1
                second = second + 1
                counter = max(0, second - first)
            else:
                second += 1
                counter += 1

        return max(maxLen, counter)
                