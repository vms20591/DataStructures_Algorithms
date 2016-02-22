N=4 #Global variable to hold the default number of rows

#Helper to check if the item is safe to place
def is_safe_to_place(board,row,col):
    #Check if any element is present in the current row from the right to left 
    i=0
    while i<col:
        if board[row][i]:
            return False
        i+=1
    
    #Check if any element is present in the upper diagonal
    i=row
    j=col
    while i>=0 and j>=0:
        if board[i][j]:
            return False
        i-=1
        j-=1
    
    #Check if any element is present in the lower diagonal
    i=row
    j=col
    while i<N and j>=0:
        if board[i][j]:
            return False
        i+=1
        j-=1

    return True #Says that this position is safe
    
#Solves the N-Queen problem    
def solve_board(board,col):
    if col>=N:
        return True #All the queens have been placed
    
    row=0
    while row<N:
        if is_safe_to_place(board,row,col):
            board[row][col]=1 #This place is safe
            
            if(solve_board(board,col+1)): #Now proceed in this route
                return True #This says that the configuration worked
                
            board[row][col]=0 #Backtrack point. Since, this configuration didn't work, restore it.
        row+=1
        
    return False #If this point is reached then the configuration didn't work

#Print the board
def print_board(board):
    for row in board:
        print(row)

#Kicks off the flow
def main(n):
    global N
    n=int(n)
    
    N=n or N #If the user enter zero default to default N which 4
    
    board=[]
    
    #Dynamically create a Board based on user input
    for i in range(N):
        row=[]
        for j in range(N):
            row.append(0)
        board.append(row)
    
    print('Unsolved Board: ')
    print_board(board)
    
    if solve_board(board,col=0):
        print("YAY!!! Solution found")
        print('Solved Board: ')
        print_board(board)
    else:
        print("No solution found :( :(")

#Kick off the flow    
main(input('Enter size of chess board N: '))