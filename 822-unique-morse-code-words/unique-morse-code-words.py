class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {"a" : ".-",
           "b" : "-...",
           "c" : "-.-.",
           "d" : "-..",
           "e" : ".",
           "f" : "..-.",
           "g" : "--.",
           "h" : "....",
           "i" : "..",
           "j" : ".---",
           "k" : "-.-",
           "l" : ".-..",
           "m" : "--",
           "n" : "-.",
           "o" : "---",
           "p" : ".--.",
           "q" : "--.-",
           "r" : ".-.",
           "s" : "...",
           "t" : "-",
           "u" : "..-",
           "v" : "...-",
           "w" : ".--",
           "x" : "-..-",
           "y" : "-.--",
           "z" : "--.."
        }
        res = set()
        for i in words:
            ans = ""
            for j in i:
                ans += morse[j]
            
            res.add(ans)
        return len(res)

            
            


        