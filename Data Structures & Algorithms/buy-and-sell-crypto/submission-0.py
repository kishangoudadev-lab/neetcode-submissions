class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = 101
        ans = 0
        for num in prices:
            x = min(x,num)
            if(ans<num-x):
                ans = num-x
        return ans