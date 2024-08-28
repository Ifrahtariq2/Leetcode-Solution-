# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lf = 1
        rt = n
        while lf < rt:
            mid = (lf +rt) // 2
            if isBadVersion(mid):
                rt = mid
            else:
                lf = mid+1
        return lf        