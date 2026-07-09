class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0])-1
        x = 0
        y = len(matrix)-1

        while(r>=0 and x<=y):
            mid = int((x+y)/2)
            if(matrix[mid][r]==target):
                return True
            elif(matrix[mid][l]<=target and matrix[mid][r]>target):
                r-=1
            elif(matrix[mid][r]<target):
                x = mid+1
            else:
                y = mid-1
                
        return False