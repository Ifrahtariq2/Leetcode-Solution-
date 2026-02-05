class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], result)
        return result

    def backtrack(self, candidates, remaining, start, current, result):
        if remaining == 0:
            result.append(current.copy())
            return

        for i in range(start, len(candidates)):

            # skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            # no need to continue if current number is too large
            if candidates[i] > remaining:
                break

            current.append(candidates[i])

            # move to next index (i + 1) since each number can be used once
            self.backtrack(candidates, remaining - candidates[i], i + 1, current, result)

            # backtrack
            current.pop()

        