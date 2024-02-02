class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(r,c,k):
            for i in range(0,9):             
                if board[i][c]==k:
                    print(board[i][c],k) 
                    return False
                if board[r][i]==k: 
                    return False
                if board[3*(r//3) + i//3][3*(c//3) + i%3]==k: 
                    return False
            return True    

        def fill(r,c):
            if r==9:
                return True
            if c==9:
                return fill(r+1,0)    
            if board[r][c]=='.':
                for k in range(1,10):
                    if isValid(r,c,str(k))==True:
                        board[r][c]=str(k)
                        if fill(r,c+1):
                            return True
                        board[r][c]='.'
                return False
            return fill(r,c+1)        

        fill(0,0)

        
