class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1] * (len(nums)+1)
        pre[0] = 1
        for i in range(len(nums)):
            pre[i+1] = nums[i]*pre[i]
        print(pre)
        suf = [1] * (len(nums)+1)
        for i in range(len(nums)):
            j = len(nums)-i-1
            suf[j-1] = nums[j]*suf[j]
        print(suf)
        res = []
        for i in range(len(nums)):
            res.append(pre[i]*suf[i])
        return res
