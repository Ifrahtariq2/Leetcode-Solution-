class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        print(len(s))
        stack = []
        for i in s:
            if i == "(" or i ==  "{" or i == "[":
                stack.append(i)
            elif (i == ")" and stack and stack[-1] == "(") :
                stack.pop()
            elif    i == "}" and stack and   stack[-1] == "{":
                stack.pop()
            elif (i == "]" and stack and stack[-1] == "["):
                stack.pop()
            else:
                return False
            
        if stack:
            return False
        return True
