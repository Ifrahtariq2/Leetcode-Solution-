class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for i in range(len(s)):
            if 97 <= ord(s[i].lower()) <= 122 or s[i].isdigit():
                new += s[i].lower()
        
        print(new[::-1])
        return new[0:len(new)] == new[::-1]

        