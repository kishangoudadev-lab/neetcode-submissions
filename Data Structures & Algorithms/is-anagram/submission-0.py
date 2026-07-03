class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] not in dict1.keys():
                dict1[s[i]] = 0
            dict1[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in dict2.keys():
                dict2[t[i]] = 0
            dict2[t[i]]+=1
        if (len(dict1) != len(dict2)):
            return False
        
        for x in dict1.keys():
            if x not in dict2.keys():
                return False
            if(dict1[x] != dict2[x]):
                return False
            
        return True