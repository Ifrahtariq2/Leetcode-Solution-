class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0
        while n > 0 :
            remainder = n % 10
            n = n // 10
            prod *= remainder
            summ += remainder
        return prod - summ    