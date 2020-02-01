import random
game = [[1,0,0,0,0,0,1],
        [1,0,0,0,0,1,1],
        [1,0,0,1,1,0,1],
        [0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0],
        [0,0,0,0,1,1,1],]

def Win(board, player):


    # check horizontal spaces
    for y in range(6):
        for x in range(4):
            if board[y][x] == player and board[y][x+1] == player and board[y][x+2] == player and board[y][x+3] == player:
                return True

    # check vertical spaces
    for y in range(3):
        for x in range(7):
            if board[y][x] == player and board[y+1][x] == player and board[y+2][x] == player and board[y+3][x] == player:
                return True


   # check / diagonal spaces
    for x in range(7):
        for y in range(3):
            if board[y][x] == player and board[y+1][x-1] == player and board[y+2][x-2] == player and board[y+3][x-3] == player:
                return True

    # check \ diagonal spaces
    for x in range(4):
        for y in range(3):
            if board[y][x] == player and board[y+1][x+1] == player and board[y+2][x+2] == player and board[y+3][x+3] == player:
                return True

    return False


x=1
def col():
    col=int(input("what you want:"))
    return(col)
def game_board(game_map, player, row, column):
    while game_map[row][column]>0:
        if row>=0:
         row=row-1
        else:
            column=col()
    print ("     0  1  2  3  4  5  6")
    game_map[row][column] = player
    for row in enumerate(game_map):
        print(row)
    return(game_map)
play = True
player=[1,2]
game_won=False
def play():

    while play:
        game = [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],]
        print ("     0  1  2  3  4  5  6")
        for row in enumerate(game):
          print(row)
          i=0
        while  x == 1:
            row_choice = 5
            if i<1:
                current_player=1
                i=i+1
                column_choice=col()
                game = game_board(game,current_player,row_choice,column_choice)
            else:
                current_player=2
                i=0
                column_choice=random.randint(0,6)
                game = game_board(game,current_player,row_choice,column_choice)
            if Win(game, current_player)== True and current_player==1:
                 print("you win ")
                 k()
            if Win(game, current_player)== True and current_player==2:
                print("you lose penis face")
            else:
                pass

def k():
    k = input("would you like to play dude")
    if k == "yes" or "ye":
        #I love you x - Uniorn you're stuck with ;*
         play()
k()
