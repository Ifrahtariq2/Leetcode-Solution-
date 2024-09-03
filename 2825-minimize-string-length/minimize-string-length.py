class Solution:
    def minimizedStringLength(self, s: str) -> int:
        stack= []
        for i in s:
            if i not in stack:
                stack.append(i)
        return len(stack)        
        