class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        zipped = zip(s,t)
        for i , j in zip(s,t):
            if i in dict1 and j != dict1[i]:
                return False     
            elif j in dict2 and i != dict2[j]:
                return False   
            else:
                dict1[i] = j
                dict2[j] = i        
        return True        