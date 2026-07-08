class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = s1+s1
        y = x[::-1]
        i = 0
        while(i<len(s1)):
            s3 = x[i:i+len(s1)]
            if(s3 in s2):
                return True
            i+=1  
        i =0      
        while(i<len(s1)):
            s3 = y[i:i+len(s1)]
            if(s3 in s2):
                return True
            i+=1
        return False