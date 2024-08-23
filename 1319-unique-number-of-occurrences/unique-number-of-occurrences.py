class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Count the occurrences of each element
        count_map = {}
        for num in arr:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        # Step 2: Check if occurrences are unique
        occurrence_set = set()
        for count in count_map.values():
            if count in occurrence_set:
                return False
            occurrence_set.add(count)
        
        return True

        