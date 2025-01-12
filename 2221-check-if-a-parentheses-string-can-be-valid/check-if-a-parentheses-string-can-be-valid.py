class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False  # A valid string must have an even length
    
    # Left-to-right pass
        balance = 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False  # More ')' than '(' at some point
    
    # Right-to-left pass
        balance = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False  # More '(' than ')' at some point
    
        return True
        
        