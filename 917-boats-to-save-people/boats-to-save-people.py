class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lf,rt = 0, len(people) -1
        boat = 0
        while (lf <= rt):
            if lf == rt:
               boat += 1
               break   
            elif people[lf] + people[rt] <= limit:
                lf += 1
                rt -= 1
                boat += 1
            else:
                boat+= 1
                rt -= 1
        return boat       
        