class Solution:
    def validPalindrome(self, s: str) -> bool:
        fp, sp = 0, len(s) - 1

        flag = False

        while fp < sp:
            if s[fp] != s[sp] and not flag:
                return self.validPal(s[fp + 1: sp + 1]) or self.validPal(s[fp: sp])
            elif s[fp] != s[sp]:
                return False
            else:
                fp += 1
                sp -= 1

        return True

    def validPal(self, s: str) -> bool:
        fp, sp = 0, len(s) - 1

        while fp < sp:
            if s[fp] != s[sp]:
                return False
            else:
                fp += 1
                sp -= 1

        return True

