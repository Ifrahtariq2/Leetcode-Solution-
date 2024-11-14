class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        dict1 = {}
        dict2 = {}
        for i,j in zip(pattern,words):
            if i in dict1 and  dict1[i] != j: 
                return False
            else:
                dict1[i] = j
            if j in dict2 and  dict2[j] !=  i:
                return False 
            else:
                dict2[j] = i
        return True                
                


        