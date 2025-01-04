class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        idx = {}
        for i , ltr in enumerate(s):
            if ltr not in idx:
                idx[ltr] = [i,i]
            else:
                idx[ltr][1] = i
        # print(idx) 
        for ltr, (first,last) in idx.items():
            if last - first > 1:
                midltr = set(s[first+1:last])
                # print(midltr)
                res +=  len(midltr)

        return res 