class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            res[key].append(i) 
        return list(res.values())
        