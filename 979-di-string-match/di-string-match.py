class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        d = len(s)
        I = 0
        res = []
        for c in s:
            if c == "I":
                res.append(I)
                I += 1
            else :
                res.append(d)
                d -= 1
        if I not in res:
            res.append(I)
        if d not in res:
            res.append(d)
        return res