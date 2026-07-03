class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = set()
        for i in range(len(nums)):
            if nums[i] in lst:
                return True
            lst.add(nums[i])
        
        return False