class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        substr = ""
        result = ""

        for i in str1:            
            substr += i
            if str1.find(substr) != -1:
                if str1.replace(substr, "") == "" and str2.replace(substr, "") == "":
                    result = substr
            else:
                return ""
        return result
       