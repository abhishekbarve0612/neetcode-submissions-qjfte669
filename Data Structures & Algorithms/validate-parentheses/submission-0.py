class Solution:
    mp = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in ['}', ']', ')']:
                if len(stk) == 0:
                    return False
                if i != self.mp.get(stk[-1]):
                    return False
                else:
                    stk.pop()
            else:
                stk.append(i)
        return len(stk) == 0
