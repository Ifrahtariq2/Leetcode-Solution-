class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for i in ransomNote:
            if i not in magazine or not ( magazine.count(i) >= ransomNote.count(i)):
                return False
        return True