class Solution:
    def addMinimum(self, word: str) -> int:
        i = 0
        res = 0 
        while i < len(word):
            count = 0
            if word[i] == "a":
                count += 1
                i += 1
            if i < len(word) and word[i] == 'b':
                count += 1
                i += 1
            if  i < len(word) and word[i] == 'c':
                count += 1
                i += 1    
            res += 3 - count
        return res