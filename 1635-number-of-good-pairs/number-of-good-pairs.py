class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hmap  = defaultdict(int)
        for i in nums:
            hmap[i] += 1
        ans = 0
        for i in hmap.values():
            if i >= 2:
                ans += (i *(i-1)) // 2
        return ans

                