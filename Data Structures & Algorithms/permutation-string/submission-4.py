class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hash = {}

        # for s in s1: hash[s] = 1 + hash.get(s, 0)

        # uniq = len(hash)

        # for idx in range(len(s2)):

        #     hash2, current = {}, 0

        #     for jdx in range(idx, len(s2)):
        #         hash2[s2[jdx]] = 1 + hash2.get(s2[jdx], 0)

        #         if hash.get(s2[jdx], 0) < hash2[s2[jdx]]:
        #             break

        #         if hash.get(s2[jdx], 0) == hash2[s2[jdx]]:
        #             current += 1

        #         if current == uniq:
        #             return True

        # ls2, ls1 = len(s2), len(s1)

        # if ls1 > ls2:
        #     return False

        # s1freq, s2freq = [0] * 26, [0] * 26

        # for idx in range(ls1):
        #     s1freq[ord(s1[idx]) - ord('a')] += 1

        #     s2freq[ord(s2[idx]) - ord('a')] += 1

        # if s1freq == s2freq:
        #     return True

        # for idx in range(ls2 - ls1):
        #     s2freq[ord(s2[idx]) - ord('a')] -= 1

        #     s2freq[ord(s2[idx + ls1]) - ord('a')] += 1

        #     if s2freq == s1freq:
        #         return True

        if len(s1) > len(s2):
            return False

        hash = {}

        for s in s1: hash[s] = 1 + hash.get(s, 0)

        hash2 = {}

        for i in range(len(s1)):
            if s2[i] in hash:
                hash2[s2[i]] = 1 + hash2.get(s2[i], 0)

        if hash2 == hash:
            return True

        fp, sp = 0, len(s1)

        while sp < len(s2):
            if s2[fp] in hash2:
                hash2[s2[fp]] -= 1
                if hash2[s2[fp]] == 0:
                    del hash2[s2[fp]]

            fp += 1
            if s2[sp] in hash:
                hash2[s2[sp]] = 1 + hash2.get(s2[sp], 0)

            if hash == hash2:
                return True

            sp += 1

        return False
