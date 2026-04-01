class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash = {}
        for c in s:
            if c in hash:
                hash[c] += 1
            else:
                hash[c] = 1

        for c in t:
            if c in hash:
                hash[c] -= 1
                if hash[c] == 0:
                    del hash[c]
            else:
                return False

        return True