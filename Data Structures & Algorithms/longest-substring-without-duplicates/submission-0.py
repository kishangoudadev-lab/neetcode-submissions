class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        group = dict()
        ans = 0
        while(l>=0 and r<len(s)):
            while(l<=r and s[r] in group):
                group[s[l]]-=1
                if(group[s[l]]==0):
                    del group[s[l]]
                l+=1
            if(s[r] not in group):
                group[s[r]] = 0
            group[s[r]] +=1
            if(ans < r-l+1):
                ans = r-l+1
            r+=1
        return ans   
            
        