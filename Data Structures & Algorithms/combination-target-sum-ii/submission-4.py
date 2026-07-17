from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        ans = []
        candidates.sort()

        self.combo(arr, ans, target, candidates, 0)

        return ans

    def combo(self, arr, ans, target, nums, index):

        if target == 0:
            ans.append(arr.copy())
            return

        if target < 0:
            return

        for i in range(index, len(nums)):

            if i > index and nums[i] == nums[i - 1]:
                continue

            if nums[i] > target:
                break

            arr.append(nums[i])

            self.combo(arr, ans, target - nums[i], nums, i + 1)

            arr.pop()