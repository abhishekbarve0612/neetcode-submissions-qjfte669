class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first, second = 0, 1
        maxLen = min(1, len(s))
        counter = maxLen
        st = set()

        if maxLen > 0:
            st.add(s[first])

        while second < len(s):
            if s[second] in st:
                maxLen = max(maxLen, counter)
                while len(st) > 0 and s[second] in st:
                    st.remove(s[first])
                    first += 1
                st.add(s[second])
                second = second + 1
                counter = max(0, second - first)
            else:
                st.add(s[second])
                second += 1
                counter += 1

        return max(maxLen, counter)
                