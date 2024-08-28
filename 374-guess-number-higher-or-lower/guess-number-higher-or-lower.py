# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lf = 0
        rt =  n      
        while lf <= rt:
            mid = (lf + rt) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                rt = mid - 1
            else:
                lf = mid + 1        
        