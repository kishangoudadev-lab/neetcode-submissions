class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = [0]*(len(nums1)+len(nums2))
        l  = 0
        r = 0
        k = 0
        while(l<len(nums1) and r< len(nums2)):
            if(nums1[l] <= nums2[r]):
                lst[k] = nums1[l]
                k+=1
                l+=1
            else:
                lst[k] = nums2[r]
                r+=1
                k+=1
        
        while(l<len(nums1)):
            lst[k] = nums1[l]
            k+=1
            l+=1        
        while(r<len(nums2)):
            lst[k] = nums2[r]
            k+=1
            r+=1
        x = int(len(lst)/2)
        if(len(lst)%2==0):
            return float((lst[x]+lst[x-1])/2)
        else:
            return float(lst[x])
            