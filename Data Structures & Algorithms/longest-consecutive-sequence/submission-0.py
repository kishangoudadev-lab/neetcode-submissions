class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set()
        for i in nums:
            st.add(i)
        ans = 0
        for i in nums:
            k = i+1
            l = 1
            while(k in st):
                l+=1
                k+=1
            ans = max(l, ans)
        return ans
