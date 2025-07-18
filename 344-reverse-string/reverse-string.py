class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """
        lf = 0
        rt = len(s) - 1
        while lf  < rt:
            if lf != rt:
                s[lf], s[rt] = s[rt],s[lf]
            lf +=1
            rt -= 1
            
        