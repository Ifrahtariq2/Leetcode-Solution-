class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1,str2):
            if str1==str2[:len(str1)] and str1==str2[-len(str1):]:
                return True
            return False
        n = len(words) 
        count = 0
        for i in range(n):
            j = i + 1
            while j < n:
                
                ans = isPrefixAndSuffix(words[i], words[j])
                if ans == True:
                    count += 1
                j+=1
                
        return count

        