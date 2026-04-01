class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        first, second = 0, 1
        match = 0

        while match < len(strs[first]) and match < len(strs[second]) and strs[first][match] == strs[second][match]:
            match += 1
        
        if match == 0:
            return ""

        for st in strs[2:]:
            if st[:match] == strs[first][:match]:
                continue
            else:
                while st[:match] != strs[first][:match]:
                    match -= 1
            if match == 0:
                return ""

        return strs[first][:match]