class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        self.subset(arr,ans,nums,0)
        return ans
    
    def subset(self, arr,ans,nums,index):
        if(index==len(nums)):
            x = arr.copy()
            ans.append(x)
            return
        
        arr.append(nums[index])
        self.subset(arr,ans,nums,index+1)

        arr.pop()

        self.subset(arr,ans,nums,index+1)