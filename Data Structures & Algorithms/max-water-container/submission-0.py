class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0;
        j = len(heights)-1
        ans = 0
        while(i<j):
            a = heights[i]
            b = heights[j]
            x = (min(a,b))*(j-i)
            if(ans<x):
                ans = (min(a,b))*(j-i)
            elif(a>b):
                j-=1
            else:
                i+=1
        return ans