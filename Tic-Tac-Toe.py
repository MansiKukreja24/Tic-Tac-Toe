# making board

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

    # Assign marker


def player_mark():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player : What is your choice? 'X' or 'O' ")
        if marker == "X" :
            return "X","O"

        else:
            return "O","X"


def place(board, marker, position):
    board[position] = marker


def win(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


import random


def choose():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space(board, position):
    return board[position] == ' '


def full(board):
    for i in range(1, 10):
        if space(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space(board, position):
        position = int(input("Choose your position (1-9):  "))
    return position


def replay():
    ans = input("Do you want to play again? 'yes' or 'no':    ")
    if ans == 'yes':
        return True
    return False


print("WELCOME TO TIC TAC TOE!!!!")

while True:
    # Reset the board
    board = [' '] * 10
    player1_marker,player2_marker = player_mark()
    turn = choose()
    print(turn + ' will go first.')

    play_game = input("Are you ready to play? Enter 'Y' or 'N'.")

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place(board, player1_marker, position)

            if win(board, player1_marker):
                display_board(board)
                print("Congratulations! you have won the game")
                game_on = False
            else:
                if full(board):
                    display_board(board)
                    print("It's a tie!!")
                    break
                else:
                    turn = 'Player 2'



        else:
            if turn == 'Player 2':
                display_board(board)
                position = player_choice(board)
                place(board, player2_marker, position)
                if win(board, player2_marker):
                    display_board(board)
                    print("Congratulations! you have won the game")
                    game_on = False
                else:
                    if full(board):
                        display_board(board)
                        print("It's a tie!!")
                        break
                    else:
                        turn = 'Player 1'
    if not replay():
        break


