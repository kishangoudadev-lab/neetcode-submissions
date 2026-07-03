class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict.keys():
                return [dict[target-nums[i]], i]
            dict[nums[i]] = i
        return [0,0]

        