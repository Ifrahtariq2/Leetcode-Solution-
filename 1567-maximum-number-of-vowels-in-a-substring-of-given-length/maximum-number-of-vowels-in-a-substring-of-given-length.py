class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s.split()
        vol = "aeiou"
        res = 0
        maxcur = 0
        for i in range(k):
            if s[i] in vol:
                maxcur +=1
        res = maxcur
            
        for i in range(k,len(s)):
            if s[i-k] in  vol:
                maxcur -= 1
            if s[i] in vol:
                maxcur +=1
            if maxcur > res:
                res = maxcur    
            
        return res     