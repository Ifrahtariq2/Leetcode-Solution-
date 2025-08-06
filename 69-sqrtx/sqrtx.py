class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        n = x // 2
        lf = 1
        rt = n
        while lf <= rt:
            mid = (lf + rt) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                lf = mid + 1
            else:
                rt = mid - 1
        return rt
        