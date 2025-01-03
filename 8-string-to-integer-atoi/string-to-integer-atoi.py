class Solution:
    def myAtoi(self, s: str) -> int:
#         s = s.strip()
        
#         res = 0
#         opr = 1
#         for i in s:
#             if i == "-" and res ==0 :
#                 opr = 1
#             if i == "+" and opr == 0:
#                 opr = 0
#             elif "0" <= i <= "9" :
#                 res = (res * 10 ) + int(i)
#             else:
#                 break
        
        
#         if opr == 1:
#             res *= -1
#         if res > (2 ** 31) - 1:
#             return (2 ** 31) - 1
#         elif  res < -(2 ** 31):
#             return -(2 ** 31)
#         return res
        s=s.strip()
        sign=0
        result=0
        flag=0
        for c in s:
            if c=='-' and flag==0:
                sign=1
                flag=1
            elif c=='+' and flag==0:
                sign=0
                flag=1
            elif c>='0' and c<='9':
                result=result*10+int(c)
                flag=1
            else:
                break
        if sign==1:
            result*=-1
        if result<-2**31:
            return -2**31
        elif result>2**31-1:
            return 2**31-1
        return result
        