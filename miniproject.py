
def printboard(): 
    for row in board:
        print(" | ".join(row))
        print("-"*(cell_size * size+(size-1) * 3))







def is_winner(pu):
    for i in range(win):
       
        if all(board[i][j]==pu for j in range(win)):
            return True
   
        if all(board[j][i]==pu for j in range(win)):
            return True
   
    if all(board[i][i]==pu for i in range(win)):
        return True
    if all(board[i][size-1-i]==pu for i in range(win)):
        return True
    return False






def full(): 
    for row in board:
        if ' ' in row:
            return False
    return True






def getmove(pu):
    while True:
        move=input(f"player {pu}, enter your move (row column): ")
        try:
            row, col=map(int, move.split())
            if 0 <= row < size and 0 <= col < size and board[row][col]==' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")





over=False
cp='X'
size=int(input("Enter the size of the board: "))
win=int(input("Enter the no of X or O required in a row to win: "))
cell_size=3 
board=[[' ' for _ in range(size)] for _ in range(size)]






while not over:
    printboard()
    row, col=getmove(cp)
    board[row][col]=cp

    if is_winner(cp):
        printboard()
        print(f"player {cp} wins!")
        over=True
    elif full():
        printboard()
        print("It's a tie!")
        over=True



    cp='O' if cp=='X' else 'X'
print("Thanks for playing!")
