class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for i in range(len(words)):
            j=0
            while j< len(words):  
                if i!=j and words[i] in words[j] and words[i] not in res:
                    res.append(words[i])
                j+=1
        return res


                  
        