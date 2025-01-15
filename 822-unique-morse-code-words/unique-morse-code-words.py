class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {
           "a" : ".-",
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
        res = []
        for i in range(len(words)):
            
            ans  = ""
            lf = 0
            while lf < len(words[i]):
                ans += morse[words[i][lf]] 
                lf += 1
            res.append(ans)
        return len(set(res))
        