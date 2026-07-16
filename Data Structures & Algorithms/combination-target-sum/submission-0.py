class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        arr = []
        nums.sort()
        self.combo(ans,arr,0,target,nums,0)
        return ans

    def combo(self,ans,arr,index,target,nums,val):
        if(target==0):
            x = arr.copy()
            ans.append(x)
            return
        if(index==len(nums) or target<0):
            return
        
        arr.append(nums[index])
        self.combo(ans,arr,index,target-nums[index],nums,0)
        arr.pop()

        self.combo(ans,arr,index+1,target,nums,0)


    