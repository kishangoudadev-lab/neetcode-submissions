class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for  i in range(len(board)):
            st = set()
            for j in range(len(board[0])):
                if(board[i][j] in st):
                    return False
                elif(board[i][j] != "."):
                    st.add(board[i][j])

        for j in range(len(board[0])):
            st = set()
            for i in range(len(board)):
                if(board[i][j] in st):
                    return False
                elif(board[i][j] != "."):
                    st.add(board[i][j]) 
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                st = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        if board[i][j] == ".":
                            continue

                        if board[i][j] in st:
                            return False

                        st.add(board[i][j])                     
        return True