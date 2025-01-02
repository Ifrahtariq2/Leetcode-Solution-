class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res =[]
        digtoword = {
            "2":"abc",
            "3": "def",
            "4": "ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        def backtrack(i, crs):
            if len(crs) == len(digits):
                res.append(crs)
                return
            for c in digtoword[digits[i]]:
                backtrack(i+1,crs+c)
        if digits:
            backtrack(0,"")
        return res