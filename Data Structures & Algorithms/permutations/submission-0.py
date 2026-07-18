class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        mem = [True] * len(nums)
        self.perm(arr, ans,mem,nums)
        return ans

    def perm(self,arr,ans,mem,nums):
        if(len(arr) == len(nums)):
            ans.append(arr.copy())
            return 
        
        for i in range(len(nums)):
            if(mem[i] == True):
                mem[i] = False
                arr.append(nums[i])
                self.perm(arr, ans,mem,nums)
                arr.pop()
                mem[i] = True


