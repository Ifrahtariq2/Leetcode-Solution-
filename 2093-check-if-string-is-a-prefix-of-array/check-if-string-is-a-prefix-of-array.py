class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        strs = ""
        
        for i in range(len(words)):
            strs += words[i]
            if strs == s:
                return True
     
        return False

        