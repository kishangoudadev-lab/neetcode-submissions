class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while(j<k):
                x = nums[i]+nums[j]+nums[k]
                if(x == 0):
                    if([nums[i],nums[j],nums[k]] not in res):
                        res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif(x>0):
                    k-=1
                else:
                    j+=1
        return res       

        