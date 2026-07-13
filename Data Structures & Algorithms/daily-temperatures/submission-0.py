class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        l = 0
        for i in range(len(temperatures)):
            x = temperatures[i]
            j = i+1
            if(j==len(temperatures)and l<len(temperatures)):
                res[l] = 0
                return res
            check = False
            while(j<len(temperatures)and l<len(temperatures)):
                if(temperatures[j]>x):
                    res[l] = abs(i-j)
                    check = True
                    l+=1
                    break
                j+=1
            if(check == False):
                res[l] = 0
                l+=1
                

        return res
                
