class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x< 0:
            return False
        ans = 0
        temp = x
        while temp>0:
            mod =  temp % 10
            ans = (ans * 10 ) + mod
            temp = temp // 10
        if ans != x:
            return False
        return True


        