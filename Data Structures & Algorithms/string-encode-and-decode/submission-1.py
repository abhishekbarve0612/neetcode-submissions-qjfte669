class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            for c in s:
                result += chr(ord(c) - 1)
            result += "-"

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        temp = ''
        for c in s:
            if c == "-":
                result.append(temp)
                temp = ''
            else:
                temp += chr(ord(c) + 1)

        if temp:
            result.append(temp)

        return result