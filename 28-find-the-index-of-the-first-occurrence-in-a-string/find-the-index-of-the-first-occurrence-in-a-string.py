class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=haystack.split(needle)

        if l[0] == '':
            return(0)
        elif l[0] == haystack:
            return(-1)
        else:
            return(len(l[0]))