class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I"   :          1,
          "V"     :     5,
         "X"       :      10,
         "L"        :    50,
         "C"     :       100,
         "D"         :    500,
          "M"    :        1000}
        summ = 0 
        
        for i in range(len(s)-1):
            curr = roman[s[i]]
            nextt = roman[s[i+1]]
            if nextt > curr:
                summ -= curr
            else:
                summ += curr
        summ += roman[s[-1]]
        return summ






        
        