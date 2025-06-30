board = [[],[],[],[],[],[], []]
running = True
drop_layer = 5
def print_board():
    for i in range(6):
        for x in range(7):
            print(board[i][x], end = '')
        print()
for i in range(7):
    for i in range(7):
        board[i].append('- ')
print_board()
turn = 'o '
while running:
    place_column = int(input("What column would you like to place your piece?: "))
    for i in range(6):
        if board[5-i][place_column] == "- ":
            board[5-i][place_column] = turn
            if turn == 'o ':
                turn = 'x '
            else:
                turn = 'o '
            for y in range(6):
                if board[y][]
                
            break

        elif board[0][place_column] == "x " or board[0][place_column] == "o ":
            print("You can't place a piece here.")
            break
        

            
        
    print_board()
   
    

    