class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        L, R = 2, x // 2

        while L <= R:
            pivot = L + (R - L) // 2
            prod = pivot * pivot

            if prod < x:
                L = pivot + 1
            elif prod > x:
                R = pivot - 1
            else:
                return pivot
        return R
