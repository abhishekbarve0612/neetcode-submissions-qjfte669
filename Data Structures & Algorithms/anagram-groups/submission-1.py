class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for st in strs:
            sth = ''.join(sorted(st))
            if sth in hash:
                hash[sth].append(st)
            else:
                hash[sth] = [st]

        result = []

        for values in hash.values():
            result.append(values)
        return result