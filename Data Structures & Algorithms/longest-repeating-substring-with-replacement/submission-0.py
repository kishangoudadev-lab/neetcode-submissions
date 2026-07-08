from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        group = dict()
        max_fre = 0
        ans = 0
        while(r<len(s)):
            if(s[r] not in group):
                group[s[r]] = 0
            group[s[r]]+=1
            max_fre = max(max_fre, group[s[r]])
            
            if((r-l+1)-max_fre>k):
                group[s[l]]-=1
                if(s[l] not in group):
                    del group[s[l]]
                l+=1
            ans = max(r-l+1,ans)
            r+=1
        return ans 
