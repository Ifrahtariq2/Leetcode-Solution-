class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Step 1: Count how many times each character appears
        char_count = Counter(s)
        
        # Step 2: Count the number of characters with an odd frequency
        odd_count = 0
        for char, freq in char_count.items():
            if freq % 2 == 1:  # If frequency is odd
                odd_count += 1
        
        # Step 3: Check if the number of palindromes (k) is possible
        # We need at least 'odd_count' palindromes to handle odd frequencies
        # We can have at most 'len(s)' palindromes (one per character)
        if odd_count <= k <= len(s):
            return True
        else:
            return False
        