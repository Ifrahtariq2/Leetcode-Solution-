class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for i in range(len(words)):
            n = len(words[i])
            good = True
            for j in range(n):
                if words[i][j] not in chars or words[i].count(words[i][j]) > chars.count(words[i][j]):
                    good = False
                    break
            if good == True:
                ans += n
        return ans