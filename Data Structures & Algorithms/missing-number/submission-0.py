class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        s2 = 0
        for i in nums:
            sum+=i
        for i in range(len(nums)):
            s2+=(i+1)

        return s2-sum
        