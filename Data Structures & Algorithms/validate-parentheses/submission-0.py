class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while(i<len(s)):
            if(s[i]=='['):
                stack.append(']')
            elif(s[i]=='{'):
                stack.append('}')
            elif(s[i]=='('):
                stack.append(')')
            elif(len(stack)>0 and stack[len(stack)-1]==s[i]):
                stack.pop()
            else:
                return False
            i+=1
        
        return len(stack)==0
        
            
                
            