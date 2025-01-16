class Solution:
    def addDigits(self, num: int) -> int:
        if 0 < num < 10:
            return num
        while num > 9:   
            nextt = 0 
            while num > 0:
        
                nextt += (num % 10)   
                num = num//10
            
            num = nextt
            
        return num