class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxfreq = Counter()
        for i in words2:
            maxfreq |= Counter(i)
        print (maxfreq)
        res = []
        
        for word in words1:
            wordfreq = Counter(word)
            check = True
            for char in maxfreq:
                
                if wordfreq[char] < maxfreq[char]:
                    check = False
                    break
            if check:
                res.append(word)
        return res

        
        