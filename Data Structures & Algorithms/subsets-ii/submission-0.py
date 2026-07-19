class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        self.sub(ans, arr, 0,nums)
        
        return ans
    
    def sub(self, ans, arr, index, nums):
        if(index == len(nums)):
            x = sorted(arr)
            if(x not in ans):
                ans.append(x)
            return
        
        arr.append(nums[index])
        self.sub(ans, arr, index+1,nums)
        arr.pop()

        self.sub(ans, arr, index+1,nums)
