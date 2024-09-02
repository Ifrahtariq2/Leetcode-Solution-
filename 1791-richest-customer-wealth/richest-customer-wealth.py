class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in range(len(accounts)):
            w = sum(accounts[i])
            if wealth < w:
                wealth = w
        return wealth    
        