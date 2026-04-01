class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash = {}

        for s in s1: hash[s] = hash.get(s, 0) + 1

        uniq = len(hash)

        for idx in range(len(s2)):
            hash2, current = {}, 0

            for jdx in range(idx, len(s2)):

                hash2[s2[jdx]] = 1 + hash2.get(s2[jdx], 0)
                
                if hash.get(s2[jdx], 0) < hash2[s2[jdx]]:
                    break

                if hash.get(s2[jdx], 0) == hash2[s2[jdx]]:
                    current += 1
                
                if current == uniq:
                    return True

        return False