import random
#display the board
def display_board(board):
    print('   |   |')
    print(' '+ board[7] +' | '+board[8]+' | '+ board[9])
    print('   |   |')
    print('--------------')
    print('   |   |')
    print(' '+ board[4] +' | '+board[5]+' | '+ board[6])
    print('   |   |')
    print('--------------')
    print('   |   |')
    print(' '+ board[1] +' | '+board[2]+' | '+ board[3])
    print('   |   |')

#input the markers
def player_input():
    marker =''
    while marker != 'X' and marker != 'O':
        marker = input("Player: Choose 'X' or 'O': ").upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

#place the marker
def place_marker(board,mark,postion):
    board[postion] = mark

#check the rows and coloumns who wins
def win_check(board,mark):
    return (
    #for rows
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[7]==mark and board[8]==mark and board[9]==mark) or
    #for columns
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark) or
    #for two diagonals
    (board[9]==mark and board[5]==mark and board[1]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark))

#random check who went first
def choose_first():
    flip = random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'

#check the space on the board if it is freely avaible or not
def space_check(board,position):
    return board[position]== ' '


#return true if the board is full
def full_board_check(board):
    for position in range(1,10):
        if space_check(board,position):
            return False
    return True

#function that asks the user for the next position and check if the position is free or not
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Enter the position (1-9): "))
    return position

#if the user want to play the game again
def replay():
    choice = input("Play again? type Yes or No: ")

    return choice == 'Yes'




print("Welcom to TIC TAC TOE")
while True:

    test_board=[' ']*10
    p1_marker,p2_marker=player_input()
    # print('Player1 Marker: ',p1_marker)
    # print('Player2 Marker: ',p2_marker)

    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input("Ready to play? y or n? ")
    if play_game=='y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn=='Player 1':
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,p1_marker,position)
            if win_check(test_board,p1_marker):
                display_board(test_board)
                print('PLAYER 1 HAS WON!!')
                game_on=False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('TIE GAME!')
                    game_on=False
                else:
                    turn='Player 2'
        else:
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,p2_marker,position)
            if win_check(test_board,p2_marker):
                display_board(test_board)
                print('PLAYER 2 HAS WON!!')
                game_on=False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('TIE GAME!')
                    game_on=False
                else:
                    turn='Player 1'

    if not replay():
        break



#test_board=['#','X','O','X','O','X','O','X','O','X']

# display_board(test_board) 

# place_marker(test_board,p1,8)
# display_board(test_board)
# print(win_check(test_board,'X'))
