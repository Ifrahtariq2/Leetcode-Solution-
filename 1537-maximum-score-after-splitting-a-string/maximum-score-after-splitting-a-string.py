class Solution:
    def maxScore(self, s: str) -> int:
        maxc = 0
        for i in range(len(s)-1):
            lf = s[:i+1]
            rt = s[i+1:]
            count = lf.count("0")+rt.count("1")
            maxc = max(maxc,count)
        return maxc    