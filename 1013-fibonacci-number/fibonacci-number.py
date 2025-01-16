class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        if n == 0:
            return first
        if n == 1:
            return second
        else:
            for i in range(2 , n+1):
                nextt = first+ second
                first = second
                second = nextt 
            return nextt